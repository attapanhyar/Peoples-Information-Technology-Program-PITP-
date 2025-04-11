# Step 1: Open the file in read mode
with open("data.txt", "r") as file:
    # Step 2: Read the file content
    content = file.read()

# Step 3: Reverse the content
reversed_content = content[::-1]

# Step 4: Write the reversed content to a new file
with open("reversed.txt", "w") as reversed_file:
    reversed_file.write(reversed_content)

print("Reversed content has been written to 'reversed.txt'")
