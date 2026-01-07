# You are running small library. Store books in list (book_list). Take name of book student want from input.If book exist in list, remove it from list and print final list by sorting but if it doesn't exist print Book,{book_name} not found.

book_list=['Maths','GK','Science','Nepali']
book_name = input("Enter the name of the book you want: ").title()

# Check if book exists in list
if book_name in book_list:
    book_list.remove(book_name)
    book_list.sort()     # sort final list
    print(f"Updated book list: {book_list}")
else:
    print(f"{book_name} book is not found.")
