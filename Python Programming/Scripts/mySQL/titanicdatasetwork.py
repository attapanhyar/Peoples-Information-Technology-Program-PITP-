# Importing necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Sample Titanic dataset (you can replace this with the actual Titanic dataset)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, None, 22, 28],
    'Sex': ['Female', 'Male', 'Male', 'Female', 'Female'],
    'Fare': [72.5, 20.0, 15.5, 8.0, 25.0],
    'Survived': [1, 0, 0, 1, 1]
}
data1 = pd.read_csv("D:/quest\AI Department/22 AI/Machine Learning/Codes/lecture 2/Titanic-Dataset.csv")

# Creating a DataFrame
df = pd.DataFrame(data)

# Step 1: Handling missing values (replacing missing 'Age' with the median)
df['Age'].fillna(df['Age'].median(), inplace=True)

# Step 2: Encoding the 'Sex' column using Label Encoding
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])

# Step 3: Normalizing numerical features (Age and Fare)
scaler = MinMaxScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Displaying the processed DataFrame
print("Preprocessed Titanic Dataset:")
print(df)
