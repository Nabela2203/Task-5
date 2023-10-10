#1. Write a python program to calculate the total number of Vowels and count each individual vowel
# A,E,I,O,U in the string 'Guvi Geeks Network Private Limited'?

text = "Guvi Geeks Network Private Limited"
text_1 = text.lower()
vowel_list = "aeiou"

count = count_a = count_e = count_i = count_o = count_u = 0

for character in text_1:
    if character in vowel_list:
        count += 1
        if character in vowel_list[0]:
           count_a +=1
        elif character in vowel_list[1]:
            count_e +=1
        elif character in vowel_list[2]:
            count_i +=1
        elif character in vowel_list[3]:
            count_o +=1
        elif character == vowel_list[4]:
            count_u +=1

print("Count_vowels: ",count)
print("Count_a: ",count_a)
print("Count_e: ",count_e)
print("Count_i: ",count_i)
print("Count_o: ",count_o)
print("Count_u: ",count_u)