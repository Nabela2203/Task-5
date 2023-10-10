#3. Write a function that takes a string and returns a new string with all vowels removed

text = input("Enter text: ") # return string
text_1 = text.lower()
vowels ="aeiou"

def string_vowels():
    for char in text_1:
        if char not in vowels:
            print(char, end="")
    print("\n")
    print(type(char))

string_vowels()