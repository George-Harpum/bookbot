"""
Program that provides some basic information around the book
- Word count
"""
def main(file):
    full_file = read_contents(file)
    count = word_count(full_file)
    letters = letter_count(full_file)
    print(f"--- Begin report of {file} ---")
    print(f"{count} words found in the document")
    sort_letters = dict(sorted(letters.items(), key=lambda x: x[1], reverse=True))
    for l, i in sort_letters.items():
        print(f"The {l!r} character was found {i} times")
    print("-- End Report ---")

def read_contents(file: str) -> str:
    with open(file) as f:
        contents = f.readlines()
    return " ".join(contents)

def word_count(string: str) -> int:
    return len(string.split())

def letter_count(string: str) -> dict[str, int]:
    dict_of_letters = {}
    for letter in string.lower():
        dict_of_letters[letter] = dict_of_letters.get(letter, 0) + 1
    return dict_of_letters

if __name__ == "__main__":
    FILE = "./books/frankenstein.txt"
    main(FILE)
