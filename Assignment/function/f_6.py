# Write a function that counts the number of characters in a string and returns the result.
# Example: If the input is Apple, the output should be { 'A': 1, 'p': 2, 'l': 1, 'e': 1 }.
def count_str(characters):
    result = {}
    for value in characters:
        result_value = result.get(value, 0) + 1
        if value in result:
            result[value] = result[value] + 1
        else:
            result[value] = 1
    return result


print(count_str("Apple"))
