CHAPTERS = {
    "RAG with LangChain - Loading Documents": {
        "overview": (
            "Retrieval Augmented Generation (RAG) improves large language models by allowing them "
            "to use external data instead of relying only on training data. "
            "This chapter covers how to load, split, embed, and store documents for retrieval."
        ),

        "sections": [
            {
                "title": "What is RAG?",
                "content": (
                    "RAG allows language models to access external data sources. "
                    "This helps overcome the limitation of fixed training data."
                )
            },
            {
                "title": "RAG Workflow",
                "content": (
                    "User query is converted into embeddings, used to retrieve relevant documents, "
                    "and those documents are added into the prompt before sending to the LLM."
                )
            },
            {
                "title": "Data Preparation",
                "content": (
                    "To use RAG, you must load documents, split them into chunks, "
                    "convert them into embeddings, and store them in a vector database."
                )
            },
            {
                "title": "Document Loaders",
                "content": (
                    "LangChain provides tools to load different file types like CSV, PDF, and HTML into memory."
                )
            },
            {
                "title": "Chunking",
                "content": (
                    "Chunking splits documents into smaller pieces. "
                    "Using chunk overlap helps preserve context between chunks."
                )
            },
            {
                "title": "Embeddings",
                "content": (
                    "Embeddings convert text into numerical vectors so that similar content can be found easily."
                )
            }
        ],

        "code_examples": [
            {
                "title": "CSVLoader Walkthrough",
                "code": """from langchain_community.document_loaders.csv_loader import CSVLoader

csv_loader = CSVLoader(file_path="path/to/your/file.csv")
documents = csv_loader.load()
print(documents)""",
                "line_explanations": [
                    {
                        "line": "from langchain_community.document_loaders.csv_loader import CSVLoader",
                        "explanation": (
                            "This line imports the CSVLoader class from LangChain so Python knows which tool to use for reading CSV files."
                        )
                    },
                    {
                        "line": 'csv_loader = CSVLoader(file_path="path/to/your/file.csv")',
                        "explanation": (
                            "This creates a CSVLoader object and points it to the CSV file you want to load."
                        )
                    },
                    {
                        "line": "documents = csv_loader.load()",
                        "explanation": (
                            "This loads the CSV data into memory as LangChain Document objects."
                        )
                    },
                    {
                        "line": "print(documents)",
                        "explanation": (
                            "This prints the loaded documents so you can inspect the output."
                        )
                    }
                ],
                "summary": (
                    "This code imports the CSV loader, connects it to a file, loads the file into LangChain, "
                    "and prints the result. This is the first step in preparing external data for a RAG system."
                )
            }
        ],

        "practice": [
            {
                "title": "CSVLoader Practice",
                "instructions": "Fill in the missing parts of the code to correctly load a CSV file using LangChain.",
                "code_template": [
                    "from langchain_community.document_loaders.csv_loader import CSVLoader",
                    "",
                    'csv_loader = ______(file_path="data.csv")',
                    "documents = csv_loader.____()"
                ],
                "blanks": [
                    {"id": 0, "answer": "CSVLoader", "options": ["CSVLoader", "PDFLoader", "TextLoader"]},
                    {"id": 1, "answer": "load", "options": ["load", "run", "execute"]}
                ],
                "explanation": "CSVLoader loads CSV files, and load() converts them into document objects."
            },
            {
                "title": "PDFLoader Practice",
                "instructions": "Complete the code to load a PDF document.",
                "code_template": [
                    "from langchain_community.document_loaders import PyPDFLoader",
                    "",
                    'loader = ______("file.pdf")',
                    "documents = loader.____()"
                ],
                "blanks": [
                    {"id": 0, "answer": "PyPDFLoader", "options": ["PyPDFLoader", "CSVLoader", "HTMLLoader"]},
                    {"id": 1, "answer": "load", "options": ["load", "read", "run"]}
                ],
                "explanation": "PyPDFLoader loads PDF files, and load() reads the content into documents."
            },
            {
                "title": "HTML Loader Practice",
                "instructions": "Fill in the missing parts to load an HTML file.",
                "code_template": [
                    "from langchain_community.document_loaders import UnstructuredHTMLLoader",
                    "",
                    'loader = ______("file.html")',
                    "documents = loader.____()"
                ],
                "blanks": [
                    {"id": 0, "answer": "UnstructuredHTMLLoader", "options": ["UnstructuredHTMLLoader", "CSVLoader", "PDFLoader"]},
                    {"id": 1, "answer": "load", "options": ["load", "parse", "run"]}
                ],
                "explanation": "UnstructuredHTMLLoader loads HTML files and extracts clean text from them."
            },
            {
                "title": "Character Text Splitter Practice",
                "instructions": "Complete the code to split text into chunks.",
                "code_template": [
                    "from langchain.text_splitter import CharacterTextSplitter",
                    "",
                    "splitter = CharacterTextSplitter(",
                    "    chunk_size=____,",
                    "    chunk_overlap=____",
                    ")"
                ],
                "blanks": [
                    {"id": 0, "answer": "100", "options": ["50", "100", "500"]},
                    {"id": 1, "answer": "10", "options": ["0", "10", "100"]}
                ],
                "explanation": "chunk_size controls chunk length, and chunk_overlap preserves context between chunks."
            },
            {
                "title": "Recursive Text Splitter Practice",
                "instructions": "Fill in the missing parts for recursive text splitting.",
                "code_template": [
                    "from langchain.text_splitter import RecursiveCharacterTextSplitter",
                    "",
                    "splitter = ______(",
                    "    chunk_size=100,",
                    "    chunk_overlap=10",
                    ")"
                ],
                "blanks": [
                    {"id": 0, "answer": "RecursiveCharacterTextSplitter", "options": ["RecursiveCharacterTextSplitter", "CharacterTextSplitter", "TextSplitter"]}
                ],
                "explanation": "RecursiveCharacterTextSplitter splits text more intelligently to preserve meaning and context."
            },
            {
                "title": "Embedding + Vector Store Practice",
                "instructions": "Complete the code to store embeddings in a vector database.",
                "code_template": [
                    "from langchain.vectorstores import Chroma",
                    "",
                    "vector_store = ______.from_documents(",
                    "    documents=chunks,",
                    "    embedding=embedding_model",
                    ")"
                ],
                "blanks": [
                    {"id": 0, "answer": "Chroma", "options": ["Chroma", "FAISS", "Pandas"]}
                ],
                "explanation": "Chroma stores embeddings so they can be searched later during retrieval."
            }
        ],

        "quiz": {
            "question": "What is the main purpose of RAG?",
            "options": [
                "To replace databases",
                "To add external data to LLM responses",
                "To delete training data",
                "To speed up coding"
            ],
            "answer": "To add external data to LLM responses",
            "explanation": "RAG allows models to use external knowledge sources, improving accuracy and relevance."
        }
    }
}