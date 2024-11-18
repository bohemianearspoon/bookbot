def count_words(str_to_count):
    words = str_to_count.split()
    return len(words)

def char_count(to_be_counted):
    count_dict = {}
    lowered_string = to_be_counted.lower()
    for i in range(0, len(lowered_string)):
        if lowered_string[i] in count_dict:
            count_dict[lowered_string[i]] += 1
        else:
            count_dict[lowered_string[i]] = 1
    return count_dict

def print_char_counts(char_string):
    char_dict = char_count(char_string)
    #char_dict.sort(reverse=True)
    sorted_dict = sorted(char_dict, key=char_dict.get, reverse=True)
    for i in sorted_dict:
        if i.isalpha():
            print(f"The '{i}' character was found {char_dict[i]} times")

def main():
    bookname = "books/frankenstein.txt"
    print(f"--- Begin report of {bookname} ---")
    with open(bookname) as f:
        file_contents = f.read()
    print (f"{count_words(file_contents)} words in the document")
    print("")
    print_char_counts(file_contents)
    print("--- End report ---")

main()
