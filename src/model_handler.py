# Import Hugging Face tools for tokenizer and model
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load tokenizer and model once when the app starts
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

# Prewritten explanations for common topics
KNOWN_EXPLANATIONS = {
    "rag": (
        "Retrieval Augmented Generation, or RAG, is a method that helps a language model answer questions using outside documents instead of relying only on what it learned during training. "
        "It works by retrieving relevant information first and then adding that information to the prompt before the model responds. "
        "A real-world example is a company chatbot that answers employee questions using internal policies, manuals, or support documents."
    ),
    "nodes and edges": (
        "Nodes and edges are the basic parts of a graph. "
        "Nodes represent things such as people, products, cities, or accounts, and edges represent the connections between them. "
        "A real-world example is a social media network, where each user is a node and each friendship or follow is an edge."
    ),
    "python loops": (
        "A loop in Python allows you to repeat code without writing it over and over. "
        "A for loop is commonly used to go through items in a list, and a while loop runs as long as a condition remains true. "
        "A real-world example is processing every row in a dataset to clean values or calculate results automatically."
    ),
    "python variables": (
        "A variable stores data in Python and gives it a name so you can use it later. "
        "Variables can hold numbers, text, lists, or larger objects like DataFrames. "
        "A real-world example is storing a customer's name, order total, or a dataset in a variable so your program can reuse it."
    ),
    "data cleaning": (
        "Data cleaning is the process of fixing missing, incorrect, or inconsistent data. "
        "It helps make a dataset more accurate and reliable before analysis. "
        "A real-world example is cleaning customer records by removing duplicates, fixing date formats, and filling in missing values before building a dashboard."
    ),
    "machine learning": (
        "Machine learning allows computers to find patterns in data and use those patterns to make predictions or decisions. "
        "Instead of coding every rule by hand, the system learns from examples. "
        "A real-world example is a movie recommendation system that suggests films based on what a user has watched before."
    ),
    "pandas dataframe": (
        "A pandas DataFrame is a table-like structure in Python with rows and columns. "
        "It is used to organize, filter, clean, and analyze data. "
        "A real-world example is loading sales data into a DataFrame so you can sort it, calculate totals, and find trends."
    ),
    "sql database": (
        "A SQL database is a structured system used to store, organize, and retrieve data using tables. "
        "SQL stands for Structured Query Language, which is used to read, insert, update, and delete data. "
        "A real-world example is an online store storing customers, products, and orders in a SQL database so the website can quickly look up and manage information."
    ),
    "sql": (
        "SQL is a language used to work with data stored in relational databases. "
        "It allows you to query data, filter results, join tables, and update records. "
        "A real-world example is using SQL to pull monthly sales data from a company database for reporting."
    ),
    "sql joins": (
        "SQL joins combine data from two or more tables based on a shared column. "
        "They are useful when related information is stored in separate tables, such as customers in one table and orders in another. "
        "A real-world example is joining customer and order tables to see which customers made which purchases."
    ),
    "api requests": (
        "An API request is a way for one application to ask another application for data or services. "
        "The request usually includes an endpoint, a method such as GET or POST, and sometimes parameters or authentication. "
        "A real-world example is a weather app sending an API request to a weather service to retrieve the current forecast."
    ),
    "recursion": (
        "Recursion is a programming technique where a function calls itself to solve a problem in smaller steps. "
        "It works best when a problem can be broken into repeating subproblems and has a clear stopping point called a base case. "
        "A real-world example is exploring folders inside folders, where the same logic is repeated for each subfolder."
    ),
    "python dictionary": (
        "A Python dictionary stores data as key-value pairs. "
        "Each key is used to look up its matching value quickly. "
        "A real-world example is storing a student's name, grade, and email in one structure so each piece of information can be accessed by name."
    ),
    "python dictionaries": (
        "A Python dictionary stores data as key-value pairs. "
        "Each key is used to look up its matching value quickly. "
        "A real-world example is storing a student's name, grade, and email in one structure so each piece of information can be accessed by name."
    ),
}

# Alternate phrasings that should map to the same concept
ALIASES = {
    "adding nodes and edges": "nodes and edges",
    "adding edges and nodes": "nodes and edges",
    "edges and nodes": "nodes and edges",
    "graph nodes and edges": "nodes and edges",
    "python loop": "python loops",
    "loops in python": "python loops",
    "variables in python": "python variables",
    "cleaning data": "data cleaning",
    "dataframe in pandas": "pandas dataframe",
    "dataframes in pandas": "pandas dataframe",
    "sql databases": "sql database",
    "database sql": "sql database",
    "sql db": "sql database",
    "joins in sql": "sql joins",
    "api request": "api requests",
    "dictionaries in python": "python dictionaries",
}

def normalize_topic(topic):
    """
    Clean user input so matching works more reliably.
    """
    return topic.strip().lower()

def match_known_topic(topic):
    """
    Match a user topic to a stored explanation when possible.
    """
    normalized = normalize_topic(topic)

    if normalized in ALIASES:
        return ALIASES[normalized]

    if normalized in KNOWN_EXPLANATIONS:
        return normalized

    for known_topic in KNOWN_EXPLANATIONS:
        if known_topic in normalized or normalized in known_topic:
            return known_topic

    if "node" in normalized and "edge" in normalized:
        return "nodes and edges"

    if "loop" in normalized and "python" in normalized:
        return "python loops"

    if "variable" in normalized and "python" in normalized:
        return "python variables"

    if "clean" in normalized and "data" in normalized:
        return "data cleaning"

    if "pandas" in normalized and "dataframe" in normalized:
        return "pandas dataframe"

    if "sql" in normalized and "join" in normalized:
        return "sql joins"

    if "sql" in normalized and "database" in normalized:
        return "sql database"

    if normalized == "sql":
        return "sql"

    if "api" in normalized and "request" in normalized:
        return "api requests"

    if "recursion" in normalized:
        return "recursion"

    if "dictionary" in normalized and "python" in normalized:
        return "python dictionaries"

    return None

def is_bad_response(text, topic):
    """
    Detect weak or broken model outputs.
    """
    cleaned = text.strip().lower()
    topic_lower = topic.strip().lower()

    bad_starts = [
        "using a",
        "describe the basics",
        "explain the concept",
        "the topic is",
        "this topic is",
    ]

    if not cleaned:
        return True

    if len(cleaned.split()) < 12:
        return True

    if cleaned == topic_lower:
        return True

    if cleaned.startswith(tuple(bad_starts)):
        return True

    if cleaned.count(".") < 1:
        return True

    return False

def generate_fallback_explanation(topic):
    """
    General-purpose fallback for technical topics.
    """
    prompt = f"""
You are a beginner-friendly coding tutor.

Write a clear explanation for: {topic}

Rules:
- Start directly with the explanation
- Do not repeat the prompt
- Use simple language
- Give 2 short paragraphs
- Paragraph 1: what it is
- Paragraph 2: one real-world example

Example style:
Topic: API
Answer: An API is a way for two software systems to communicate with each other. It allows one program to request data or services from another program in a structured way.

A real-world example is a weather app calling a weather service API to get the current forecast for a city.

Topic: SQL join
Answer: A SQL join combines rows from two tables using a related column. It helps connect information that is stored in separate tables.

A real-world example is joining a customers table and an orders table to see which customer placed each order.

Now answer this topic:
{topic}
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=220,
        do_sample=False,
        repetition_penalty=1.2
    )

    clean_text = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    if is_bad_response(clean_text, topic):
        return (
            f"{topic} is a technical concept used in programming or data systems. "
            f"It helps developers organize logic, work with data, or build software features.\n\n"
            f"A real-world example is using {topic} in an application, script, or data workflow to solve a practical problem more efficiently."
        )

    return clean_text

def explain_concept(topic):
    """
    Main function used by the app.
    First tries a stored explanation.
    If none is found, it generates a general technical explanation.
    """
    matched_topic = match_known_topic(topic)

    if matched_topic:
        return KNOWN_EXPLANATIONS[matched_topic]

    return generate_fallback_explanation(topic)