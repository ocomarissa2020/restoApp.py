# Activity 1

name = input('Enter Full Name: ')
mathGrade = int(input('Enter Math Grade: '))
scienceGrade = int(input('Enter Science Grade: '))
englishGrade = int(input('Enter English Grade: '))
average = float((mathGrade+scienceGrade+englishGrade)/3)

print()
print('Name:',name)
print('Math:',mathGrade)
print('Science:',scienceGrade)
print('English:',englishGrade)
print('Average:',average)


if average >= 75:
    print('Congratulations, you passed the semester.')
    if mathGrade < 75:
        if scienceGrade < 75:
            print ('But you need to re-enroll in Math and Science subject.')
        elif englishGrade < 75:
            print ('But you need to re-enroll in Math and English subject.')
        else:
            print('But you need to re-enroll in Math subject.')
    elif scienceGrade < 75:
        if mathGrade < 75:
            print ('But you need to re-enroll in Math and Science subject.')
        elif englishGrade < 75:
            print ('But you need to re-enroll in Science and English subject.')
        else:
            print('But you need to re-enroll in Science subject.')
    elif englishGrade < 75:
        if scienceGrade < 75:
            print ('But you need to re-enroll in English and Science subject.')
        elif mathGrade < 75:
            print ('But you need to re-enroll in Math and English subject.')
        else:
            print('But you need to re-enroll in English subject.')
else:
    print ('Sorry, you failed the semester.')

  
  