# def name():
import random

first_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
middle_names = ['A','B','C','D','E','F','G','H','I','J']
last_names = ['Sun', 'Mercury', 'Venus','Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus','Neptune', 'Pluto']
names = []

print('=====Name Generator=====')
response = str(input('Generate Name: Y if Yes, N if No: '))
while response.upper() == 'Y' or response.upper() == 'N' :
    if response.upper() == 'Y':
        for item in range(1):
            r = random.randint(0,10)
            a = first_names[r]
            b = middle_names[r]
            c = last_names[r]
            full_name = str(a)+" "+str(b)+". "+str(c)
            print('Congratulations! Your new name is: ',full_name)
            names.append(full_name)
    elif response.upper() == 'N':
        print('\nThanks!\n')
        for name in names:
            print(name)
        break
    else:
        print('Invalid Option Selected! Application Terminated.')
        break
    response = str(input('Generate Name: Y if Yes, N if No: '))











