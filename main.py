import string

def print_report(name:str, words_count:int, letter_count:dict):
    print(f"--- Begin report of books/{name} ---")
    print(f"{words_count} words found in the document")
    letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse = True))

    for letter in letter_count:
        print(f"The \'{letter}\' character was found {letter_count[letter]} times")
    print("--- End report ---")

def count_words(words):
    return len(words)

def count_letters(words):
    letter_count = {}
    for word in words:
        for letter in word:
            if letter not in string.ascii_lowercase:
                continue
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
    return letter_count

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contens = file_contents.lower()
        words = file_contents.split()

        letter_count = count_letters(words)
        words_count = count_words(words)

        print_report("frankenstein.txt", words_count, letter_count)

if __name__ == "__main__":
    main()
