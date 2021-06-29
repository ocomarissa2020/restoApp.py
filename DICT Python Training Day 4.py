
# Day 4

a = 1
while a <= 10:
    print(a)
    a += 1

names = ["Mike", "Ana", "Jun"]
for name in names:
    print(name)

names = ["Naruto", "Luffy", "Nami", "Sasuke"]
for name in names:
    if name != "Eren":
        print('Name is', name)

for a in range(10, 20):
    print(a)

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('Current fruit:', fruits[index])

# Break Statements
num = 0
while num <= 10:
    if num == 5:
        break
    num += 1
    print(num)
print('The loop has been terminated')

#ContinueStatements
num = 0
while num <= 10:
    num += 1
    if num == 5:
        continue
    print(num)

# Pass Statement

name = 'Marissa Oco'
for letter in name:
    if letter == 'o':
        pass


numbers = [1,2,3,4,5]
print(numbers)
numbers.append(99)
