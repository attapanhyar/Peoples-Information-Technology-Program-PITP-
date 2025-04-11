# Step 1: Get user input
user_input = input("Enter a sentence to write to the file: ")

# Step 2: Open the file in write mode and write the user input
with open("output.txt", "w") as file:
    file.write(user_input)

# Step 3: Open the file in read mode and read the content
with open("output.txt", "r") as file:
    content = file.read()

# Step 4: Print the content that was written to the file
print("Content of the file:")
print(content)
