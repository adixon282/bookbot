import sys
from stats import get_book_text
from stats import word_count
from stats import get_chars
from stats import counts
from stats import sort_chars




def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1) 
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = word_count()
        chars_dict = get_chars()
        sorted_chars = sort_chars()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"{num_words}")
    print("--------- Character Count -------") 
    for entry in sorted_chars:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main()
