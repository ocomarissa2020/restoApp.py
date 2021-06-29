print("=====Calculator App=====")
try:
    num1 = int(input('Enter First Number: '))
except ValueError:
    print("Invalid Entry. Another error will terminate the program.")
    num1 = int(input('Enter First Number: '))
try:
    num2 = int(input('Enter Second Number: '))
except ValueError:
    print("Invalid Entry. Another error will terminate the program.")
    num2 = int(input('Enter Second Number: '))
option = input('Select Operation\n[A] Add\n[B] Subtract\n[C] Multiply\n[D] Divide\n[Any Key to Exit] ')

while option.upper() != 'A' or option.upper() != "B" or option.upper() != "C" or option.upper() != "D":
    if option.upper() == 'A':
        try:
            print(num1 + num2)
        except ValueError:
            print("Value Error")
        except TypeError:
            print("Type Error")
    elif option.upper() == 'B':
        try:
            print(num1 - num2)
        except ValueError:
            print("Value Error")
        except TypeError:
            print("Type Error")
    elif option.upper() == 'C':
        try:
            print(num1 * num2)
        except ValueError:
            print("Value Error")
        except TypeError:
            print("Type Error")
    elif option.upper() == 'D':
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("Error! Division by Zero")
    else:
        print('Exit Application. Thank You!')
        break
    response = input('Do you want to try again? Y for Yes, any Key to Exit: ')
    if response.upper() != 'Y':
        print('Thanks!')
        break
    try:
        num1 = int(input('Enter First Number: '))
    except ValueError:
        print("Invalid Entry. Another error will terminate the program.")
        num1 = int(input('Enter First Number: '))
    try:
        num2 = int(input('Enter Second Number: '))
    except ValueError:
        print("Invalid Entry. Another error will terminate the program.")
        num2 = int(input('Enter Second Number: '))
    option = input('Select Operation\n[A] Add\n[B] Subtract\n[C] Multiply\n[D] Divide\n[Any Key to Exit] ')
