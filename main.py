#takes a string and returns the number of words delimited on whitespace.
def count_words(book):
    return len(file_contents.split())



#takes a string and returns a dict of string -> int
#each character that appears in the string will be a key, with its value being the number of occurences
def count_characters(file_contents):
    character_counts = {}
    for c in file_contents:
        c = c.lower()
        if c in character_counts:
            character_counts[c] +=1
        else:
            character_counts[c] = 1

    return(character_counts)


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

wc_frankenstein = count_words(file_contents)
print(f"the word count for Frankenstein is: {wc_frankenstein}")

cc_frankenstein = count_characters(file_contents)
print("A list of the characters in Frankenstein with their frequency:")
print(cc_frankenstein)

