# This file stores quiz questions and checks answers

# Dictionary of quiz questions by topic
QUIZ_QUESTIONS = {
    "Python Basics": {
        "question": "What does a variable do in Python?",
        "options": [
            "Repeats code automatically",
            "Stores data for later use",
            "Deletes errors in a program",
            "Connects to a database"
        ],
        "correct_answer": "Stores data for later use",
        "explanation": (
            "A variable stores information in Python so it can be reused later. "
            "For example, you can store a name, number, or list in a variable."
        )
    },
    "Loops": {
        "question": "What is the main purpose of a loop in Python?",
        "options": [
            "To repeat code",
            "To create images",
            "To rename variables",
            "To shut down the program"
        ],
        "correct_answer": "To repeat code",
        "explanation": (
            "Loops are used to repeat code instead of writing the same logic many times. "
            "This is useful when working with lists, datasets, or repeated tasks."
        )
    },
    "Data Cleaning": {
        "question": "Which task is part of data cleaning?",
        "options": [
            "Adding random errors",
            "Removing duplicates",
            "Ignoring missing values",
            "Deleting all columns"
        ],
        "correct_answer": "Removing duplicates",
        "explanation": (
            "Data cleaning includes fixing missing values, removing duplicates, "
            "and correcting inconsistent formats so the data becomes more reliable."
        )
    },
    "Machine Learning": {
        "question": "What does machine learning help computers do?",
        "options": [
            "Learn patterns from data",
            "Physically repair hardware",
            "Create internet cables",
            "Replace all databases"
        ],
        "correct_answer": "Learn patterns from data",
        "explanation": (
            "Machine learning helps systems find patterns in data and use them "
            "to make predictions or decisions."
        )
    },
    "Pandas": {
        "question": "What is a pandas DataFrame most similar to?",
        "options": [
            "A web browser",
            "A spreadsheet table",
            "A password manager",
            "A computer mouse"
        ],
        "correct_answer": "A spreadsheet table",
        "explanation": (
            "A pandas DataFrame organizes data into rows and columns, much like "
            "a spreadsheet, but with powerful coding features."
        )
    }
}


def get_quiz_topics():
    """
    Return the list of available quiz topics.
    """
    return list(QUIZ_QUESTIONS.keys())


def get_quiz_by_topic(topic):
    """
    Return the quiz data for the selected topic.
    """
    return QUIZ_QUESTIONS.get(topic)


def check_answer(selected_answer, correct_answer):
    """
    Compare the user's selected answer to the correct answer.
    Returns True if correct, otherwise False.
    """
    return selected_answer == correct_answer