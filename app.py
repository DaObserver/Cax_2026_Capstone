# ---------------------------------
# Imports
# ---------------------------------
import streamlit as st

from src.model_handler import explain_concept
from src.chapter_data import CHAPTERS

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="Class Companion",
    page_icon="📘",
    layout="wide"
)

# ---------------------------------
# Session State
# ---------------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "questions_answered" not in st.session_state:
    st.session_state.questions_answered = 0

if "answered_topics" not in st.session_state:
    st.session_state.answered_topics = set()

# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.write("✨ Your AI-powered study assistant")
st.sidebar.markdown("---")

# ---------------------------------
# Main Header
# ---------------------------------
st.title("📘 Class Companion")
st.caption("Learn concepts, break down chapters, and practice like a real developer.")

# ---------------------------------
# Tabs
# ---------------------------------
tab1, tab2, tab3 = st.tabs([
    "Concept Explainer",
    "Chapter Mode",
    "Practice Mode"
])

# =================================
# TAB 1: Concept Explainer
# =================================
with tab1:
    st.subheader("Concept Explainer")
    st.write("Enter any coding or technical topic.")

    topic = st.text_input(
        "Enter a topic:",
        placeholder="Example: SQL databases",
        key="concept_input"
    )

    if st.button("Explain Topic"):
        if topic.strip():
            with st.spinner("Generating explanation..."):
                explanation = explain_concept(topic)

            st.success("Done!")
            st.markdown("### Explanation")
            st.write(explanation)
        else:
            st.warning("Please enter a topic.")

# =================================
# TAB 2: Chapter Mode
# =================================
with tab2:
    st.subheader("Chapter Mode")

    chapter_names = list(CHAPTERS.keys())
    selected_chapter = st.selectbox("Choose a chapter:", chapter_names)

    chapter = CHAPTERS[selected_chapter]

    # Overview
    st.markdown("## Overview")
    st.write(chapter["overview"])

    st.markdown("---")

    # Sections
    st.markdown("## Concepts")
    for section in chapter["sections"]:
        with st.expander(section["title"]):
            st.write(section["content"])

    st.markdown("---")

    # Code Walkthrough
    st.markdown("## Code Walkthroughs")
    for example in chapter["code_examples"]:
        with st.expander(example["title"]):

            st.code(example["code"], language="python")

            st.markdown("### Line-by-Line Explanation")
            for item in example["line_explanations"]:
                st.markdown(f"**{item['line']}**")
                st.write(item["explanation"])

            st.markdown("### Summary")
            st.info(example["summary"])

    st.markdown("---")

    # Quiz
    st.markdown("## Chapter Quiz")

    quiz = chapter["quiz"]

    st.write(f"**Question:** {quiz['question']}")

    answer = st.radio(
        "Choose an answer:",
        quiz["options"],
        key=f"quiz_{selected_chapter}"
    )

    if st.button("Submit Answer"):

        if selected_chapter not in st.session_state.answered_topics:

            st.session_state.questions_answered += 1
            st.session_state.answered_topics.add(selected_chapter)

            if answer == quiz["answer"]:
                st.session_state.score += 1
                st.success("Correct! 🎉")
            else:
                st.error("Incorrect")

            st.info(quiz["explanation"])
            st.write(f"Correct Answer: {quiz['answer']}")

        else:
            st.warning("Already answered this chapter.")

# =================================
# TAB 3: Practice Mode (UPGRADED)
# =================================
with tab3:
    st.subheader("Practice Mode")
    st.write("Fill in the missing code like a real developer.")

    chapter_names = list(CHAPTERS.keys())
    selected_chapter = st.selectbox(
        "Choose a chapter:",
        chapter_names,
        key="practice_select"
    )

    chapter = CHAPTERS[selected_chapter]

    if "practice" in chapter:

        for exercise in chapter["practice"]:

            with st.expander(exercise["title"]):

                st.write(exercise["instructions"])

                st.markdown("### Code")

                # Show full code block
                formatted_code = "\n".join(exercise["code_template"])
                st.code(formatted_code, language="python")

                st.markdown("### ✍🏽 Fill in the blanks")

                user_answers = []

                for blank in exercise["blanks"]:
                    user_input = st.text_input(
                        f"Blank {blank['id'] + 1}",
                        placeholder="Type answer...",
                        key=f"{exercise['title']}_{blank['id']}"
                    )
                    user_answers.append(user_input.strip())

                if st.button("Check Answer", key=exercise["title"]):

                    correct = True

                    for i, blank in enumerate(exercise["blanks"]):
                        if user_answers[i].lower() != blank["answer"].lower():
                            correct = False

                    if correct:
                        st.success("Correct! 🎉")
                        st.balloons()
                    else:
                        st.error("Try again.")

                    st.info(exercise["explanation"])

    else:
        st.warning("No practice exercises available.")