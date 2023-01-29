def print_upper_words(words,must_start_with):
    """Takes a list of words then converts the words to uppercase and prints it out"""


    for word in words:
        if word.startswith(must_start_with):
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],("h","y"))