#9. Write a function that takes a string and returns the number of words in it.

str_1 = input("Enter the string: ") # am nabela hello

def number():
    count = 0
    # split - remove all the spaces and return list ['am', 'nabela', 'hello'] - 3
    for words in str_1.split():
        count +=1
        print(words)
    print(count)

number()