# Calculate and display the file sizes of python.txt and java.txt in KB. (Hint: Use the os library; you may use AI tools for help.)


import os

# Get file sizes in bytes
python_size = os.path.getsize("python.txt")
java_size = os.path.getsize("java.txt")

# Convert bytes to KB
python_size_kb = python_size / 1024
java_size_kb = java_size / 1024

# Display the results
print(f"Size of python.txt: {python_size_kb:.2f} KB")
print(f"Size of java.txt: {java_size_kb:.2f} KB")
