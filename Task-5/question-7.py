#7. Write a function that takes a string and returns the most frequent character in it. - how many times a particular character is present in that string
# hello - "l" is the most frequent character
# dictionary -key = get

str = input("Enter string: ")
str_1 = str.lower()
d = {}

def frequent():
    for char in str_1:
        if char not in d:
            d[char] = 1
        else:
            d[char] +=1
    print(d)
    print(max(d, key=d.get)) # return key name with max values

frequent()