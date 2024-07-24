def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #lower_case = text.lower()
    words = word_count(text)
    c_count = character_count(text)
    sorted_dict = sort_dict(c_count)
    #print(text)
    #print(words)
    #print(lower_case)
    #print(c_count)
    print(sorted_dict)
    
    
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
        #  key.isalpha() determines if key in new_set is an alphabetic character (==True)
        if key.isalpha():
            character_dict[key] = character_list.count(key)
    return character_dict
    #print(new_set)

#  Entire function first creates a list of dictionaries, then sorts by new designated keys, returning the list of dictionaries
def sort_dict(x):
    list_of_dict = []
    #  iterates through existing dictionary, creates a new "temp_dict" to wrap the existing dictionary with new keys mapped to the key/value pair
    for key,value in x.items():
        temp_dict = {"letter": key, "num":value}
        list_of_dict.append(temp_dict)

    #  blanket function to sort a dictionary by a key. In this case, the key is "num"
    def sort_on(dict):
        return dict["num"]    
    
    #  uses the sort_on function to sort the list_of_dict by number, starting at the highest first
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict


main()

'''
copy from the boot.dev site
# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]
vehicles.sort(reverse=True, key=sort_on)
print(vehicles)
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
'''