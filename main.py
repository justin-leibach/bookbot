def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #lower_case = text.lower()
    words = word_count(text)
    c_count = character_count(text)
    #print(text)
    #print(words)
    #print(lower_case)
    print(c_count)
    

#character_dict = {}
    
#  Uses book_path variable as a file handle to open file and read text    
def get_book_text(path):
    with open(path) as f:
        return f.read()

#  Counts all words from text found in book
def word_count(x):
    y = x.split()
    return len(y)

#  Convert all text into lowercase, create a set to eliminate duplicates, initialize dictionary, populate with unique set items, count unique set items
def character_count(x): 
    lower_case = x.lower()
    character_list = list(lower_case)
    new_set = set(character_list)
    character_dict = {}
    for key in new_set:
        character_dict[key] = character_list.count(key)
    return character_dict
    #print(new_set)


main()

#should I use a set with some sort of iteration to populate a dictionary?
#how do i populate the list without manually iterating a-z?