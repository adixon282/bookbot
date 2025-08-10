import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = len(text.split())
    wc_message = f"Found {num_words} total words"
    return wc_message

def get_chars():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    lower_text = text.lower()
    char_count = {}
    for letter in lower_text:
        if letter.isalpha():
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1
    return char_count

def counts(letters):
    return letters["num"]

def sort_chars():
    char_count_list = []
    char_dict = (get_chars())
    for letter in char_dict:
        num = char_dict[letter]
        char_count_list.append({"char": letter, "num": num})
    char_count_list.sort(reverse=True, key=counts)
    return char_count_list

    #return chardict.sort(reverse=True, key=counts)