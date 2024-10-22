def main():
    file_path = 'books/frankenstein.txt'

    book_text = get_book_text(file_path)
    num_words = get_count_words(book_text)
    
    print(f"{num_words} words in the document!")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_words(str):
    words = str.split()
    return len(words)




main()