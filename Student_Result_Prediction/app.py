import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Title
st.title("Student Result Prediction System")

# Load dataset
data = pd.read_csv("student_data.csv")

# Input and output
X = data[['marks', 'attendance']]
y = data['result']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.write("Model Accuracy:", round(accuracy * 100, 2), "%")


st.subheader("Enter Student Details")

# User inputs
marks = st.number_input("Marks", min_value=0, max_value=100)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100)

# Prediction
if st.button("Predict Result"):
    input_data = pd.DataFrame(
    [[marks, attendance]],
    columns=['marks', 'attendance']
)

    result = model.predict(input_data)


    if result[0] == 1:
        st.success("Prediction: PASS ✅")
    else:
        st.error("Prediction: FAIL ❌")
