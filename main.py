def main():
    book_path = "books/frankenstein.txt"

    print_report(book_path)
    

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lowered_text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alph_dict = {}
    for i in alphabet:
        alph_dict[i] = lowered_text.count(i)
    return alph_dict

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(alph_dict):
    list_dict = []
    for i in alph_dict:
        list_dict.append({"letter":i,"num":alph_dict[i]})
    list_dict.sort(reverse=True,key=sort_on)
    return list_dict

def print_report(book_path):
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    nb_words = get_num_words(text)
    print(f"{nb_words} words found in the document.")
    print()
    alph_dict = get_num_characters(text)
    list_dict = chars_dict_to_sorted_list(alph_dict)
    for i in list_dict:
        letter = i["letter"]
        if not letter.isalpha():
            continue
        num = i["num"]
        print(f"The '{letter}' character was found {num} times")
    print("--- End report ---")
    
main()