# Create a new file named java.txt. Copy the content from python.txt, but replace the word Python with Java.

with open("python.txt", "r") as file:
    content = file.read()

updated_content = content.replace("Python", "Java")

with open("java.txt", "w") as file:
    file.write(updated_content)

print("java.txt created successfully.")
