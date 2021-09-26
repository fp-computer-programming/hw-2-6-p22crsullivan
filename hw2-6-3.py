# Author: CRS 9/26/21
text1 = input("Please enter the number of free throws scored ")
text2 = input("Please enter the number of 2 pointers scored ")
text3 = input("Please enter the number of 3 pointers scored ")
freeThrows = int(text1)
twoPointers = int(text2) * 2
threePointers = int(text3) * 3
totalScore = freeThrows + twoPointers + threePointers
print(totalScore)
