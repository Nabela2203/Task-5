#6. Write a function that takes two strings and return the longest common substring between them. 1. abcdef 2.zbcdf => bcd
# sequence - non consequitive - S1 = “AGGTAB”, S2 = “GXTXAYB” - The longest subsequence which is present in both strings is “GTAB”- 4
# substring -  consequitive - longest common substring- abcjklp, acjkp => cjk -3

def longest_common_substring(str1, str2): #("abcdefg", "bcdfgh")
    l1 = len(str1) #7
    l2 = len(str2) #6
    max_length = 0
    end_index = 0

    for i in range(l1): # 0,1,2,3,4,5,6
        for j in range(l2): # 0,1,2,3,4,5
            length = 0
            while (i + length<l1) and (j + length <l2) and (str1[i+length] == str2[j+length]):
                length+=1
            if length>max_length:
                    max_length = length
                    end_index = i

    longest_substring = str1[end_index:end_index+max_length]
    print(longest_substring)

longest_common_substring("abcdefg", "bcdfgh")