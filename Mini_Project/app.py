import streamlit as st

st.title("Marks Average Analyzer")

marks = st.text_input("Enter marks separated by commas (e.g. 78,85,90)")

if st.button("Analyze"):
    marks_list = list(map(float, marks.split(",")))

    average = sum(marks_list) / len(marks_list)
    highest = max(marks_list)
    lowest = min(marks_list)

    st.success("Analysis Completed")
    st.write("Marks:", marks_list)
    st.write("Average Marks:", average)
    st.write("Highest Marks:", highest)
    st.write("Lowest Marks:", lowest)
