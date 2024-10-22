def main():
    file_path = 'books/frankenstein.txt'

    book_text = get_book_text(file_path)
    num_words = get_count_words(book_text)
    chars_dict = get_char_dict(book_text)

    print_report(file_path, num_words, chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    
    text_lower = text.lower()
    for char in text_lower:
        if not chars.get(char):
            chars[char] = 0
        
        chars[char] += 1

    return chars

def sort_on(dict):
    return dict["count"]

def print_report(name, words_count, char_dict):
    print(f"--- Begin report of {name} ---")
    print(f"{words_count} words found in the document")
    print()

    char_list = []
    for char, count in char_dict.items():
        if not char.isalpha():
            continue

        char_list.append({"char": char, "count":count})
    
    char_list.sort(reverse=True, key=sort_on)
    for char_obj in char_list:
        print(f"The '{char_obj["char"]}' character was found {char_obj["count"]} times")

    print("--- End report ---")


main()