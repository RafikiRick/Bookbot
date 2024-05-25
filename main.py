def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    letter_list = dict_to_list(letter_count)
    letter_list.sort(reverse=True, key=sort_on)
    report(letter_list, word_count, book_path)

def report(letter_list, word_count, path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for item in letter_list:
        print(f"The '{item['letter']}' character was found {item['num']} times")
    print("--- End report ---")

def sort_on(item):
    return item["num"]

def dict_to_list(letter_count):
    list_of_dicts = [{"letter": k, "num": v} for k, v in letter_count.items()]
    return list_of_dicts

def get_letter_count(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower in letter_counts:
                letter_counts[char_lower] += 1
            else:
                letter_counts[char_lower] = 1
    return letter_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

main()
