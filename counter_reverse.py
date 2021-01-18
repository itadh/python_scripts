#!/usr/bin/python3
numbers = ['1,2,3,4,5,6,7,8,9,10']
numbers = ['1','2','3','4','5','6','7','8','9','10']
numbers = [1,2,'3',4,5,6,7,8,9,10]
numbers = [1,2,3,4,5,6,7,8,9,10]
anzahl = len(numbers) - 1
# for loop
for teil in numbers:
    print(numbers[anzahl])
    anzahl = anzahl - 1
# while loop
print('-'*30)
i = len(numbers) - 1
while i >= 0:
    print(numbers[i])
    i = i - 1
#    i -= 1

