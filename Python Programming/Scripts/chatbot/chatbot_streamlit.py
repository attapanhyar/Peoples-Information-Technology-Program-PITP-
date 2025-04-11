import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import streamlit as st

# Load dataset
data_path = "C:/Users/Atta/Downloads/customer-support-llm-chatbot-training-dataset-main/customer-support-llm-chatbot-training-dataset-main/data/Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv"
data = pd.read_csv(data_path)
# print(data.columns)
# Preprocess the dataset
# data = data[['Question', 'Answer']].dropna()
X = data['instruction']
y = data['response']

# Vectorize the data
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train a model
model = MultinomialNB()
model.fit(X_train, y_train)

# Streamlit app
st.title("SBBU Nawabshah")
st.write("How can we Hellp You?")

# Chatbot function
def get_response(user_input):
    user_input_vector = vectorizer.transform([user_input])
    predicted_answer = model.predict(user_input_vector)
    return predicted_answer[0]

# Chat UI
if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

user_input = st.text_input("You: ", key="input")

if st.button("Send") or user_input:
    if user_input:
        bot_response = get_response(user_input)
        st.session_state["conversation"].append(("You", user_input))
        st.session_state["conversation"].append(("Bot", bot_response))

# Display conversation
for speaker, message in st.session_state["conversation"]:
    if speaker == "You":
        st.write(f"**{speaker}:** {message}")
    else:
        st.write(f"_{speaker}:_ {message}")
