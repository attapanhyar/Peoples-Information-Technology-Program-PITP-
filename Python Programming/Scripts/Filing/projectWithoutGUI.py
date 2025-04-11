import os

# Function to open and read the content of a file
def open_file():
    file_path = input("Enter the file path to open: ")

    try:
        with open(file_path, "r") as file:
            content = file.read()  # Read file content
            print("\n--- File Content ---")
            print(content)  # Display file content

        # After reading, the file pointer will be at the end of the file
        print(f"\nFile pointer is at position: {file.tell()} (end of file)")

        return file_path  # Return the path of the opened file

    except FileNotFoundError:
        print("Error: File not found!")
        return None

# Function to write new content to the file
def write_file(file_path):
    if file_path is None:
        print("Error: No file is open to write.")
        return

    try:
        with open(file_path, "w") as file:
            content = input("Enter the content you want to write to the file: ")
            file.write(content)  # Write content to the file
            print("File has been updated successfully.")

    except Exception as e:
        print(f"Error while writing to file: {e}")

# Function to check file pointer position
def check_file_pointer(file_path):
    if file_path is None:
        print("Error: No file is open to check pointer.")
        return

    try:
        with open(file_path, "r") as file:
            file.seek(0, os.SEEK_END)  # Move pointer to the end of the file
            position = file.tell()  # Get current pointer position
            print(f"File pointer is currently at byte: {position} (end of file)")

    except Exception as e:
        print(f"Error while checking file pointer: {e}")

# Main menu to run the file reader and writer application
def main():
    file_path = None

    while True:
        print("\n--- File Handling Menu ---")
        print("1. Open and read a file")
        print("2. Write to a file")
        print("3. Check file pointer position")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            file_path = open_file()

        elif choice == '2':
            write_file(file_path)

        elif choice == '3':
            check_file_pointer(file_path)

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option! Please select 1, 2, 3, or 4.")

# Start the file handling program
if __name__ == "__main__":
    main()
