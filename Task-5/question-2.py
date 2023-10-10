#2. Create a pyramid of numbers from 1 to 20 using for loop?

for i in range(1,21): #1,2,3,.........20
    print() # 20 - space
    for j in range(1, i+1): #range(1,2)=>1, (1,3) -> 1,2, (1,4) =>1,2,3
        print(j, end=" ") # print in rows