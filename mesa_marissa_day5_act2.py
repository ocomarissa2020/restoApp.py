word = str(input('Enter a word be to reversed: '))


def reverse(word):
    print('INPUT:', word)
    print('OUTPUT:', word[::-1].upper(), '(', len(word), 'characters)')

(reverse(word))