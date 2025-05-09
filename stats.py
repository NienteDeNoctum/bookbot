def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    # create an empty dictionary to store chars
    char_counts = {}

    # loop through each character in the text
    for char in text:
        # convert character to lowercase
        char = char.lower()

        # add/update count in dictionary
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # return the completed dictionary
    return char_counts

def chars_dict_to_sorted_list(char_counts):
    # crerated a list to hold the dictionaries
    result = []

    # Convert each key-value pair to a dictionary and add to the list
    for char, count in char_counts.items():
        result.append({"char": char, "num": count})
    
    # Sort the list by count (num) in descending order
    result.sort(reverse=True, key=lambda x: x["num"])
    
    return result