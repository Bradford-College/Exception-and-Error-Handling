'''
Open a text file, read the contents, and handle the FileNotFoundError if the file does not exist. 
Always close the file using the finally block.
'''

file = None
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file is not None:
        file.close()