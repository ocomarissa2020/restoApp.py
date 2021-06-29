class Reservation(object):
    def __init__(self, name, date, time, adults, children, total):
        self.name = str(name)
        self.date = str(date)
        self.time = str(time)
        self.adults = int(adults)
        self.children = int(children)
        self.total = float(total)

    def createRT(self):
        return (rNum, self.date, self.time, self.name.upper(), self.adults, self.children, self.total)


reservation = {}
t_adult = {}
t_child = {}
o_total = {}
rNum = 0


def viewReservation():
    print('\n***View Reservation')
    if len(reservation) == 0:
        print("There are no reservation in the current session!\n")
    else:
        print("#ID\t\t  Date\t\t  Time\t\t  Name\t\t  No. of Adults\t\t  No. of Children\n")
        for item in reservation:
            items = reservation.get(item)
            for i in items[:-1]:
                print(f"{i}", end="\t\t")
            print("\n")
    # a = input('Enter [Y] to open reservation.txt file: ')
    # if a == 'Y':
    #     file = open("reservation.txt", "r")
    #     print(file.read())
    #     file.close()


def makeReservation():
    print('\n***Make Reservation')
    try:
        name = str(input("Enter Name: "))
        date = str(input("Enter Date(DD-MM-YYYY): "))
        time = str(input("Enter Time(HH:MM): "))
        adults = int(input("No. of Adults: "))
        children = int(input("No. of Children: "))
        total = adults * 500 + children * 300
        t_adult[rNum] = adults
        t_child[rNum] = children
        o_total[rNum] = total
        reserve = Reservation(name.upper(), date, time, adults, children, float(total))
        res = (reserve.createRT())
        reservation[rNum] = res
        for item in reservation:
            items = reservation.get(item)
            for i in items[:-1]:
                with open("reservation.txt", "a") as file:
                    file.write(str(i) + '\t\t')
                    print("\n")
                    file.close()
        print(
            f"\nReservation successfully created!\n Reservation Number: {rNum}\n Name: {name.upper()}\n Date: {date}\n Time: {time}\n No. of Adults: {adults}\n No. of Children: {children}")
    except ValueError:
        print("There is an incorrect input. Please check!\n")


def deleteReservation():
    print('\n***Delete Reservation')
    resd = int(input("Enter Reservation Number: "))
    ans = str(input('Are you sure you want to cancel? [Y]/[N]: '))
    if ans.upper() == 'Y':
        try:
            del reservation[resd]
            del t_adult[resd]
            del t_child[resd]
            del o_total[resd]
            print('Reservation', resd, 'successfully deleted.\n')
        except KeyError:
            print("Not Found. Invalid Reservation ID.\n")
    elif ans.upper() == 'N':
        print('Reservation', resd, 'deletion has been cancelled.\n')
    else:
        print('Invalid Entry! Application Cancelled.')


def generateReport():
    print('\n***Generate Report')
    print("#ID\t\t  Date  \t\t\tTime  \t\tName  \t\tNo. of Adults  \t\tNo. of Children  \t\tSub Total\n")
    for item in reservation:
        items = reservation.get(item)
        for i in items:
            print(f"{i}", end="\t\t")
        print("\n")

    print('\nTotal Number of Adults: ', sum(t_adult.values()))
    print('Total Number of Children: ', sum(t_child.values()))
    print('Grand Total: ', sum(o_total.values()), '\n')


def exit():
    print('Exit Application. Thanks!')


def clearTxt():
    file = open("reservation.txt", "r+")
    file.truncate(0)
    file.close()


print("=====RESTAURANT RESERVATION SYSTEM=====")
option = input(
    ' [A] View All Reservation\n [B] Make Reservation\n [C] Delete Reservation\n [D] Generate Report\n [E] Exit\n Select: ')
while option.upper() != 'A' or option.upper() != "B" or option.upper() != "C" or option.upper() != "D":
    if option.upper() == 'A':
        viewReservation()
    elif option.upper() == 'B':
        makeReservation()
        rNum += 1
    elif option.upper() == 'C':
        deleteReservation()
    elif option.upper() == 'D':
        generateReport()
    elif option.upper() == 'E':
        exit()
        break
    else:
        print('Invalid Selection. Application Closed.')
        break
    option = input(
        'Select Menu\n [A] View All Reservation\n [B] Make Reservation\n [C] Delete Reservation\n [D] Generate Report\n [E] Exit\n Select: ')
clearTxt()
