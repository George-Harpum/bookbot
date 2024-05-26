"""
Program that provides some basic information around the book
- Word count
"""
def main(file):
    full_file = read_contents(file)
    count = word_count(full_file)
    return count

def read_contents(file: str) -> str:
    with open(file) as f:
        contents = f.readlines()
    return " ".join(contents)

def word_count(s: str):
    return len(s.split())

if __name__ == "__main__":
    FILE = "./books/frankenstein.txt"
    print(main(FILE))

