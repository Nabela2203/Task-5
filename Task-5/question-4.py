#4. Write a function that takes a string and returns the number of unique characters in it-characters that occur only once

unique = input("Enter string: ")
uni_char = unique.replace(" ","")
print(uni_char)
unique_char = uni_char.lower()
print(unique_char)
length = len(unique_char)
print("length", length)
length_set= len(set(unique_char))
print("length_set", length_set)

def char():
    # set -mutable (modified), no-index, sorted order, dupilcates are ignored (no error, but only one value is considered)
    if length == length_set:
        return True
    else:
        return False

print(char())