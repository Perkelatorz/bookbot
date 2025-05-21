def get_num_words(book):
    book_text = book.split()
    num = 0
    for text in book_text:
        num += 1
    return num


def get_char_number(text):
    lower_case = text.lower()
    values = {}
    for char in lower_case:
        if char not in values:
            values[char] = 1
        else:
            values[char] += 1
    return values


def sort_on(dict):
    return dict["num"]


def report_format(num_chars_dict):
    sorted_list = []
    for value in num_chars_dict:
        sorted_list.append({"char": value, "num": num_chars_dict[value]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
