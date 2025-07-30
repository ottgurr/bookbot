import sys
from stats import (
    count_words,
    count_characters,
    sort_list
)

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    text = get_book_text(file_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_list = sort_list(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        if not entry["char"].isalpha():
            continue
        print(f"{entry["char"]}: {entry["num"]}")
    
    print("----------- Word Count ----------")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()
