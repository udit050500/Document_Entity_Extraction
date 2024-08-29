import streamlit as st
import os
import pandas as pd
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Streamlit app
st.set_page_config(page_title="SchemaXtract", page_icon=":bar_chart:", layout="wide")
st.title("📊 PDF Document Entity Extraction App")

st.markdown(
    "Upload a PDF, set your desired response schemas, and let the app generate structured outputs for the entities you need using advanced AI models."
)

# Step 1: Upload PDF File
st.sidebar.subheader("Upload Your PDF")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    # Create a directory to store the uploaded PDF
    upload_dir = "./uploads/"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Save the uploaded file to the directory
    file_path = os.path.join(upload_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success(f"File saved to {file_path} 📄")
    
    # Preview PDF Upload
    st.markdown("### Uploaded File Preview")
    with st.expander("Click to preview uploaded PDF"):
        st.write(f"File Name: {uploaded_file.name}")
        st.write(f"File Size: {uploaded_file.size/1024:.2f} KB")
    
    # Step 2: Input Response Schemas
    st.markdown("### Define Response Schemas")
    st.info("Enter the name and description for each response schema.", icon="ℹ️")

    num_schemas = st.number_input("Number of Response Schemas", min_value=1, step=1, value=3)

    response_schemas = []
    for i in range(num_schemas):
        with st.expander(f"Response Schema {i+1}", expanded=True):
            schema_name = st.text_input(f"Entity {i+1} Name", key=f"name_{i}")
            schema_description = st.text_input(f"Entity {i+1} Description", key=f"description_{i}")
            if schema_name and schema_description:
                response_schemas.append(ResponseSchema(name=schema_name, description=schema_description))
    
    # Step 3: Process the PDF and Generate Output
    if st.button("🚀 Generate Output") and response_schemas:
        with st.spinner("Processing the document and generating output..."):
            try:
                # Load PDF from the saved file path
                docs = PyMuPDFLoader(file_path).load()

                # Split the PDF into manageable chunks
                splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                    model_name="gpt-4o-mini", chunk_size=10000, chunk_overlap=1000
                )
                docs = splitter.split_documents(docs)

                # Setup LLM and prompt
                llm = ChatOpenAI(model="gpt-4o-mini")
                output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
                format_instructions = output_parser.get_format_instructions()

                prompt = PromptTemplate(
                    template="Answer the following questions using the docs provided: \n{docs}\n{format_instructions}\n",
                    partial_variables={"format_instructions": format_instructions, "docs": docs},
                )

                # Generate output using the chain
                chain = prompt | llm | output_parser
                output = chain.invoke({})

                # Step 4: Display the Output in the requested format (Schema name - Answer)
                st.markdown("### Generated Output")
                st.success("Output generated successfully! 🎉", icon="✅")

                # Convert the output into a list of key-value pairs and display as a table
                results = [{"Entity Name": key, "Response": value} for key, value in output.items()]
                results_df = pd.DataFrame(results)

                # Display the results as a table
                st.table(results_df)

                # Option to download the output in JSON format
                st.download_button(
                    label="💾 Download Output as JSON",
                    data=results_df.to_json(orient="records"),
                    file_name="output.json",
                    mime="application/json"
                )

            except Exception as e:
                st.error(f"An error occurred: {e}", icon="🚨")
