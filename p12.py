import os
filename = "hello2.txt"
try:
    # Trying to access a file that does not exist
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print("FileNotFoundError:", e)
