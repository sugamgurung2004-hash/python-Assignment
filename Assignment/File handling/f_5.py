# Find and display the most frequently repeated word in python.txt.

with open("python.txt", "r") as file:
    text = file.read()

words = text.lower().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Find the most frequently repeated word
most_frequent_word = max(word_count, key=word_count.get)

# Display result
print("Most frequently repeated word:", most_frequent_word)
print("Frequency:", word_count[most_frequent_word])
