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

# **DRAFT** Convert all text into lowercase, create a set to eliminate duplicates, create dictionary and populate with unique set items ***
#   Still need to add counts to the dictionary using the unique keys (?how to add to dict, how to iterate?)
def character_count(x): 
    lower_case = x.lower()
    character_list = list(lower_case)
    new_set = set(character_list)
    character_dict = dict.fromkeys(new_set, 0)
    #for i in new_set:
        
    
    return character_dict
    #print(new_set)


main()

#should I use a set with some sort of iteration to populate a dictionary?
#how do i populate the list without manually iterating a-z?