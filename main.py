#takes a string and returns the number of words delimited on whitespace.
def count_words(book_string):
    return len(book_string.split())



#takes a string and returns a dict of string -> int
#each character that appears in the string will be a key, with its value being the number of occurences
def count_characters(book_string):
    character_counts = {}
    for c in book_string:
        c = c.lower()
        if c in character_counts:
            character_counts[c] +=1
        else:
            character_counts[c] = 1

    return(character_counts)


def generate_report(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    print("\n---Beginning of report---\n")
    book_wc = count_words(file_contents)
    print(f"{book_wc} words were found in the document.")
    book_cc = count_characters(file_contents)
    #dict.items() returns a view object which can be iterated over, so we can use sorted():
    sorted_cc = {k: v for k, v in sorted(book_cc.items(), reverse=True, key=lambda item: item[1])}
    print("\nFrequency for each letter:")
    for c in sorted_cc:
        if c.isalpha():
            print(f"{c} occured {sorted_cc[c]} times.")
    print("\n---end of report---\n")



book_path = "books/frankenstein.txt"
generate_report(book_path)
