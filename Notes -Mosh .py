# Python Tutorial
# print("Hello World")
# variables
# string, integer, float
# casting - int, str, float, bool

# num1 = float(input('First: '))
# num2 = float(input('Second: '))
# sum = num1+num2
# print('sum: ', float(sum))

# name = "Marissa"
# # print(name.upper())
# print("Mar" in name)

# operator
# / - return integer
# // - return false
# % - modulo
# ** - return exponent

# increment (arithmetic)
# x = 10
# x += 3
# x-= 3
# x*= 3

# operator precedence
# >
# <
# >=
# <=
# ==
# !=
# price = 25
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)
# and, or, not

# temp = 35
#
# if temp > 30:
#     print ('hot')
# elif temp > 20:
#     print ('warm')
# else:
#     print('cold')
# print('Done')

# weight = input("Weight: ")
# unit = input("(K)g or (L)bs: ")
# if unit.upper() == "K":
#     converted = float(weight) / 0.45
#     print("Weight in Lbs: ", converted)
# else:
#     converted = float(weight) * 0.45
#     print("Weight in Kg: ", converted)

# loops
# i = 1
# while i <= 10:
#     print(i * '*')
#     i += 1

# list
# names = ["John", "Bob", "Sam", "Mary"]
# print(names)
# print(names[0])
# print(names[-1])
# names[0] = "Jon"
# print(names)
# print(names[0:3])
# print(names)
#
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6) -add element to list
# print(numbers)
# numbers.insert(0, "Hello") - update an element
# print(numbers)
# numbers.remove("Hello") - remove an element
# print(numbers)
# numbers.clear() - delete elements
# print(numbers)
# print(4 in numbers) - find element
# print(len(numbers)) - find how many elements

# for number in numbers:
#     print(number)
# for name in names:
#     print(name)
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1
range
nums = range(5)
for num in nums:
    print(num)
nums = range(5,20,2)
for num in nums:
    print(num)
for num in range(10,20,3):
    print(num)

tuples - unchangeable
unpacking
coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x,y,z =coordinates
print(x)


# dictionaries
# name = {
#     "first_name" : "",
#     "middle_name" : "",
#     "last_name" : "",
# }
# # print('DOB: (date_of_birth) ', customer.get("birthdate", "Feb 15, 1989"))
# print('Full Name (first_name): ', name["first_name"])
# print('Middle Name (middle_name): ', name["middle_name"])
# print('Last Name (last_name): ', name["last_name"])


key = input('Enter Key: ')
value = input('Enter Value: ')
name[key] = value
print('Full Name (first_name): ', name["first_name"])
print('Middle Name (middle_name): ', name["middle_name"])
print('Last Name (last_name): ', name["last_name"])

# phone = input ("Phone: ")
# digits_mapping = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4":"four"
# }
#
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch,"!") + " "
# print(output)
