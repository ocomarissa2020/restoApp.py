# Day 4 Act 3

word = str(input('Enter word: '))
response = str(input('Do you want to add another word? Y if Yes, N if No: '))
wordBank = [word]

if response == 'Y' or response == 'y':
    while response == 'Y' or response == 'y':
        word = str(input('Enter word: '))
        wordBank.append(word)
        response = str(input('Do you want to add another word? Y if Yes, N if No: '))
        continue
if response == 'N' or response == 'n':
    print('Congratulations! You now have', len(wordBank), 'word/s in your WordBank')
    print(wordBank)
else:
    print('Invalid Choice. Application Terminated!')
