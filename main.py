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

def print_report(wc, letters):
     pass

def main():
        book_path = "books/frankenstein.txt"
        file_contents = open_book(book_path)
        # print(file_contents)
        count_letters(file_contents)
        print(count_letters(file_contents))

main()