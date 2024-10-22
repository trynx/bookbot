def main():
    file_path = 'books/frankenstein.txt'

    book_text = get_book_text(file_path)
    num_words = get_count_words(book_text)
    chars_dict = get_char_dict(book_text)

    print(f"{num_words} words in the document!")
    print(chars_dict)

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



main()