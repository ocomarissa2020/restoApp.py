# Day 3, Activity 2

print ('PBB Calculator\n')

office = input('Enter Office: ')
years = int(input('How many years in service? '))

if years >= 10 and office == 'IT':
    print ('Bonus: ', 10000)
elif years >= 10 and office == 'ACCT':
    print ('Bonus: ', 12000)
elif years >= 10 and office == 'HR':
    print ('Bonus: ', 15000)
elif years < 10 and office == 'IT':
    print ('Bonus: ', 5000)
elif years < 10 and office == 'ACCT':
    print ('Bonus: ', 6000)
elif years < 10 and office == 'HR':
    print ('Bonus: ', 7500)
else:
    print ('You are not eligible for a bonus.')