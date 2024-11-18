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
    for i in char_dict:
        print(f"{i}: {char_dict[i]}")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print (f"This book contains {count_words(file_contents)} words.")
    print("Counts of the book's characters are:")
    print_char_counts(file_contents)

main()
