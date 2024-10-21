#Counts of all words in document

import string
from collections import Counter

def count_words_in_file(file_path):
    # Create a counter to store word counts
    word_count = Counter()

    # Open the file and read its content
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Remove punctuation and convert to lowercase
        text = text.translate(str.maketrans("", "", string.punctuation)).lower()

        # Split the text into words
        words = text.split()

        # Update the word counts
        word_count.update(words)

    return word_count

# Specify the path to your text document
file_path = input("Enter the path to the text document: ")
word_counts = count_words_in_file(file_path)

# Print the word counts from largest to smallest
for word, count in word_counts.most_common():
    print(f"'{word}': {count}")
