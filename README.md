# PDF Budget Analysis App with LLM-Powered Entity Extraction

## Overview

This project is a PDF Budget Analysis application that allows users to upload PDF files, define response schemas (entities), and generate structured outputs using LLMs. The application is designed to extract specific information from the documents, such as key financial metrics, and display them in a table format for easy viewing and analysis. The app is built using Streamlit for the frontend and integrates with OpenAI's LLM for generating entity-based responses.

## Features

- **PDF Upload and Analysis**: Upload PDF files and define response schemas to extract key information using LLMs.
- **Structured Output**: The app generates structured outputs based on the defined entities, displayed in a user-friendly table.
- **JSON Download**: Easily download the output as a JSON file for further analysis.
- **Responsive UI**: Built with Streamlit, providing a smooth and intuitive interface.

## Tech Stack

- **Python**
- **Langchain**
- **OpenAI GPT-4**
- **Streamlit**
- **PyMuPDF for PDF Processing**
- **Natural Language Processing (NLP)**
- **Web Application Development**

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.12
- `pip` package manager

### Clone the Repository

```bash
git clone https://github.com/your-username/pdf-budget-analysis-app.git
cd pdf-budget-analysis-app
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root directory and add the following environment variable for OpenAI API:

```
OPENAI_API_KEY=your_openai_api_key
```

Alternatively, Streamlit Cloud will automatically handle this if you use the secrets manager.

### Running the Application

#### Start the Streamlit Application

```bash
streamlit run Document_Entity_Extraction.py
```

## Usage

### Upload PDF Files

1. Navigate to the Streamlit application.
2. Upload your PDF files using the sidebar uploader.
3. Click "Submit & Process" to save and preview the uploaded PDF.

### Define Response Schemas

1. Specify the number of response schemas you want to define (e.g., "Total Revenue", "Profit Margin").
2. For each schema, provide a name and a description.
3. Click "Generate Output" to analyze the PDF and extract the requested information.

### View and Download Results

1. The results will be displayed as a table on the main page.
2. You can download the output in JSON format for further use.

## Project Structure

```
Document_Entity_Extraction/
│
├── Document_Entity_Extraction.py          # Streamlit application code
├── requirements.txt                       # Python dependencies
└── README.md                              # Project documentation
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Langchain](https://github.com/langchain/langchain)
- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
```
