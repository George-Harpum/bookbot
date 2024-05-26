"""
Program that provides some basic information around the book
- Word count
"""
def main(file):
    full_file = read_contents(file)
    return full_file

def read_contents(file: str) -> str:
    with open(file) as f:
        contents = f.readlines()
    return " ".join(contents)

if __name__ == "__main__":
    FILE = "./books/frankenstein.txt"
    print(main(FILE))
