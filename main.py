def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    #print(text)
    print(words)
    
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(x):
    y = x.split()
    return len(y)

main()