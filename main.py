from stats import word_count
from stats import character_count
from stats import character_report
import sys

def main():
    text = get_book_text(sys.argv[1])
    words = word_count(text)
    unique_count = character_count(text)
    report = character_report(unique_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char_dict in report:
        character = char_dict["char"]
        if character.isalpha():
            count = char_dict["num"]
            print(f"{character}: {count}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()