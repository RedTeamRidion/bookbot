from stats import word_count

def main():
    text = get_book_text("books/frankenstein.txt")
    words = word_count(text)
    print(f"{words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()