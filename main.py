def words_count(content):
    words_list = content.split()
    count = len(words_list)
    return count

def open_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def count_letters(content):
    raw = content
    lowered_content = raw.lower()
    char_list = list(lowered_content)
    letters_dict = {}
    value = 1
    for char in char_list:
        if not(char in letters_dict):
            letters_dict[char] = value
        else:
            count = letters_dict[char]
            letters_dict[char] = count+1
    return letters_dict

def print_report(path, wc, letters):
     print(f"--- Begin report of {path} ---")
     print(f"{wc} words found in the document\n")
     for letter in letters:
        print(f"The {letter} character was found {letters[letter]} times")
     print("--- End Report ---")    
    

def clean_dict(content):
     new_dict = {}

     for dict in content:
          if dict.isalpha():
            # new_dict = {"name":dict,"num":content[dict]}
            # dict_list.append(new_dict)
            new_dict[dict] = content[dict]
     return new_dict
    
def sort_highest(d, reverse = True):
     return dict((sorted(d.items(), key = lambda x: x[1], reverse = reverse)))

def main():
        book_path = "books/frankenstein.txt"
        file_contents = open_book(book_path)
        w_count = words_count(file_contents)
        letters_d = count_letters(file_contents)
        clean = clean_dict(letters_d)
        print_report(book_path, w_count, sort_highest(clean))
        # print(sort_highest(clean))

main()