# Open python.txt and add the line “I will learn Error Handling next” at the end of the file.


with open("python.txt", "a") as file_object:
    file_content = file_object.write("I will learn error handling next.")
