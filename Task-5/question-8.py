#8. Write a function that takes a string and returns True if it is an anagram of other string, False otherwise
# anagram - eg - keen - knee , heart - earth

str_1 = input("Enter 1st string: ")
str_2 = input("Enter 2nd string: ")

def anagram():
    # sorted() - alphabet order - aehrt -(  heart - earth )
     if ((len(str_1) == len(str_2)) and (sorted(str_1) == sorted(str_2))):
         return True
     else:
         return False

print(anagram())