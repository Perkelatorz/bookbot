import sys

from stats import get_char_number, get_num_words, report_format


def main():
    if sys.argv.__len__() < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_num = get_char_number(text)
    order_list = report_format(char_num)
    print_report(book_path, num_words, order_list)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def print_report(book_path, num_words, order_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in order_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")


main()
