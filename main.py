def count_words(str_to_count):
    words = str_to_count.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print (f"This book contains {count_words(file_contents)} words.")
main()
