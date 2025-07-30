from stats import count_words, count_characters, sort_list
import sys
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

file_path = sys.argv[1]

def main(): 
    text = get_book_text(file_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_list = sort_list(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        char = entry["char"]
        num = entry["num"]
        if entry["char"].isalpha() != True:
            del entry 
        else:
            print(f"{char}: {num}")
    print("----------- Word Count ----------")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()
