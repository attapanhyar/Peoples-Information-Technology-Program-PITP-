import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

# Sample dataset of intents and responses
data = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "how are you", "good morning", "good evening"],
        "responses": ["Hello! How can I help you?", "Hi there!", "Hey! What's up?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "take care"],
        "responses": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "thanks a lot", "appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Glad I could help!"]
    },
    "age": {
        "patterns": ["how old are you", "your age", "what's your age"],
        "responses": ["I’m as old as the technology I’m built with!", "Age is just a number for me!"]
    }
}

# Prepare training data
labels = []
sentences = []

for label, intent in data.items():
    for pattern in intent["patterns"]:
        labels.append(label)
        sentences.append(pattern)

# Vectorize the input data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)
y = np.array(labels)

# Train the model
model = MultinomialNB()
model.fit(X, y)

# Function for chatbot response
def chatbot_response(user_input):
    user_input_vector = vectorizer.transform([user_input])  # Vectorize user input
    prediction = model.predict(user_input_vector)  # Predict the intent
    intent = prediction[0]  # Get the predicted intent

    # Fetch a random response for the predicted intent
    responses = data[intent]["responses"]
    return random.choice(responses)

# Chatbot loop
print("Chatbot: Hi! I'm your friendly chatbot. Type 'exit' to end the chat.")
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    try:
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
    except Exception as e:
        print("Chatbot: I'm not sure I understand. Can you rephrase?")
