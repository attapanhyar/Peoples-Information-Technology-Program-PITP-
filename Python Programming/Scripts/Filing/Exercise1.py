

# Step 1: Open the file in read mode
with open("students.txt", "r") as file:
    # Step 2: Loop through each line in the file
    for line in file:
        # Step 3: Print each line (end="" removes extra newlines)
        print(line, end="")
