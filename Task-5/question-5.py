#5. Write a function that takes a string and returns True if it is a palindrome, False otherwise.
# palindrome -"121" “civic,” “madam,” “radar,” and “deified.”, A man, a plan, a canal: Panama! (a man a plan a canal panama)

text = input("Enter string: ")
#slicing - index - 0(default), position - last (default), step - positive +1 or reverse -1
pal_str = text[::-1]

def palindrome():
    if (text == pal_str):
        print("True, Palindrome")
    else:
        print("False, Not a palindrome")

palindrome()