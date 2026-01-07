#count number of vowels in a given sentence

vowels=input("Enter the vowel:")
vowels = vowels.lower()
count_vowels=vowels.count('a') + vowels.count('e')+vowels.count('i')+vowels.count('o')+vowels.count('u')
print(count_vowels)