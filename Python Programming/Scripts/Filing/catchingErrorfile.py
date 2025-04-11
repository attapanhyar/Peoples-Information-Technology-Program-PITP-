

try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found!")


position = file.tell()
file.seek(0)


