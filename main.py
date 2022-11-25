def count_words(book):
    return len(file_contents.split())


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

wc_frankenstein = count_words(file_contents)
print(f"the word count for Frankenstein is: {wc_frankenstein}")

