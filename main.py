import sys
from stats import count_words, count_chars, chars_dict_to_sorted_list

# Check if a book path was provided
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from command line arguments
path = sys.argv[1]

# Define the path to the book
path = sys.argv[1]

# Read the file using the path variable
with open(path, 'r') as file:
    book_text = file.read()

# Count the words
word_count = count_words(book_text)

# Count the characters
char_counts = count_chars(book_text)

# get sorted list of character dictionaries
sorted_chars = chars_dict_to_sorted_list(char_counts)



# Print the result
print("============== BOOKBOT ============== ")
print("Analyzing book found at books/...")
print("------------- Word Count -------------")
print(f"Found {word_count} total words")
print("----------- Character Count ----------")

# print each alphabetical character and its count
for char_dict in sorted_chars:
    char = char_dict["char"]
    count = char_dict["num"]
    if char.isalpha():
        print(f"{char}: {count}")

print("============= END ===============")
