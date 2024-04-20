def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()
        
    num_words = count_words(text)
    letters_dict = count_letters(text)
    letters_sorted_list = sorted_list_of_letter_dict(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in letters_sorted_list:
        print(f"The '{item["letter"]}' character was found {item["count"]} times")

    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered_text = text.lower()
    letter_dict = {}
    for letter in lowered_text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["count"]
    
def sorted_list_of_letter_dict(text):
    dict_letters = count_letters(text)
    list_dict = []
    for letter in dict_letters:
        if letter.isalpha():
            list_dict.append({"letter": letter, "count": dict_letters[letter]})
    list_dict.sort(reverse = True, key = sort_on)
    return list_dict


main()