# Day 4 Act 2

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
total = num1 + num2
print('The sum of number 1 and number 2 is', total, '.')
response = str(input('Do you want to try again? Y/y if Yes, N/n if No: '))

if response == 'y' or response == 'Y':
    while response == 'y' or response == 'Y':
        num1 = int(input('Enter number 1: '))
        num2 = int(input('Enter number 2: '))
        print('The sum of number 1 and number 2 is', total, '.')
        response = str(input('Do you want to try again? Y/y if Yes, N/n if No: '))
        continue
print('Thank You!')
