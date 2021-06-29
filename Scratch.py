print('\n==========Add Record==========')
name = input('Enter Name: ')
email = input('Email: ')
address = input('Address: ')
user_input = ('\nName: ' + name.upper() + '\nEmail: ' + email + '\nAddress: ' + address)
print(user_input)
file = open("file.txt", "a")
file.write(user_input)
file.close()
print('File has been updated.\n')

print('\n==========View Records==========')
file = open("file.txt", "r")
print(file.read())
file.close()


print('\n==========Clear All Records==========')
        file = open("file.txt", "r+")
        file.truncate(0)
        file.close()
        print('\n==========No Records Found==========')

print('Thank You!')
break



class Student(object):
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def student_average(self):
        math = int(self.math)
        science = int(self.science)
        english = int(self.english)
        average = (math + science + english) / 3
        if average > 75:
            rating = "Passed"
        else:
            rating = "Failed"
        print ("Name: ", self.name, "\nMath: ", self.math, "\nScience: ", self.science, "\nEnglish: ", self.english,
              "\nAverage:", average,"(",rating,")")


name = input("Enter Full Name: ")
math = int(input('Enter Math Grade: '))
science = int(input('Enter Science Grade: '))
english = int(input('Enter English Grade: '))
stud1 = Student(name.upper(), math, science, english)
stud1.student_average()



class House (object):
    def __init__(self, floorSize,noOfFloors,noOfDoors ):
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors
    def switchOn(self):
        print ('The switch is On.')
    def lightOpen(self):
        print('The light is Open.')
    def ovenOpen(self):
        print('The oven is Open.')






#classes

reservation ={}
reservationNumber = 0

class Reservation(object):
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = adults
        self.children = children

    def showReservation(self):
        print(self.name + '\t\t' + self.date + '\t\t',self.time,'\t\t'+ self.adults + '\t\t'+ self.children)

def viewReservation():
    print('=====View Reservation=====')
    file = open("reservation.txt", "r")
    print(file.read())
    file.close()
def makeReservation():
    print('=====Make Reservation=====')
    name = input(str('Enter Name: '))
    date = input(str('Enter Date: '))
    time = input(str('Enter Time: '))
    adults = input('Enter No. of Adults: ')
    children = input('Enter No. of Children: ')
    reservation = Reservation(name,date,time,adults,children)
    r1 = reservation.showReservation()
    file = open("reservation.txt", "a")
    file.write(str(r1))
    file.close()
    print('File has been updated.\n')

def deleteReservation():
    print('=====Delete Reservation=====')
    file = open("reservation.txt", "r+")
    file.truncate(0)
    file.close()
    print('\n==========No Records Found==========')
def generateReport():
    print('=====Generate Report=====')
    print()
def exit():
    print('Exit Application. Thanks!')


print("=====RESTAURANT RESERVATION SYSTEM=====")
option = input('Menu\n [A] View All Reservation\n [B] Make Reservation\n [C] Delete Reservation\n [D] Generate Report\n [E] Exit\n Select: ')

while option.upper() != 'A' or option.upper() != "B" or option.upper() != "C" or option.upper() != "D":
    if option.upper() == 'A':
        viewReservation()
    elif option.upper() == 'B':
        makeReservation()
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
    option = input('Select Menu\n [A] View All Reservation\n [B] Make Reservation\n [C] Delete Reservation\n [D] Generate Report\n [E] Exit\n Select: ')















reservation = {}
rnum = 0

while True:
mylist= []
choice = input('\nRESTAURANT RESERVATION SYSTEM\nSystem Menu\na. View all Reservationsn\nb. Make Reservation\nc. Delete Reservation\nd. Generate Report\ne. Exit\nEnter choice --> ').lower()
if(choice == "a"):
if (len(reservation) == 0):
print("There are no reservations!!")
else:
print("#Date\t\t\tTime\t\tName\tAdults\tChildren")
for item in reservation:
list = reservation.get(item)
for i in list[:-1]:
print(f"{i}", end="\t\t")
print("\n")
elif(choice =="b"):
try:
rnum += 1
name = input("Enter Name: ")
Date = input("Enter date(DD-MM-YYYY): ")
Time = input("Enter time(HH:MM): ")
adults = int(input("Number of adults: "))
Children = int(input("Number os children: "))
total = adults*500 + Children*300
reservation[rnum]= [Date,Time,name,adults,Children,total]

print("\nBelow are your Reservation Details:")
print(f"Reservation Number\t\t{rnum}\nName\t\t{name}\nDate\t\t{Date}\nTime\t\t{Time}\nTotal Adults\t\t{adults}\nTotal children\t\t{Children}\n")
print(reservation)

except ValueError:
print("there is an incorrect value!! try again")


elif(choice == "c"):
getindex = 0;
rnumd = int(input("Enter Reservation number:"))
try:
reservation.pop(rnumd)
except KeyError:
print("Invalid reservation ID")

print("Reservation deleted")

elif(choice == "d"):
print("#Date\t\t\tTime\t\tName\tAdults\tChildren\tSubtotal")
for item in reservation:
for i in reservation.get(item):
print(f"{i}",end="\t")
print("\n")
elif(choice == "e"):
break


reservation = {}
rnum = 0

while True:
mylist= []
choice = input('\nRESTAURANT RESERVATION SYSTEM\nSystem Menu\na. View all Reservations\nb. Make Reservation\nc. Delete Reservation\nd. Generate Report\ne. Exit\nEnter choice --> ').lower()
f1 = open("reservation.txt", "a")
if(choice == "a"):
if (len(reservation) == 0):
print("There are no reservations!!")
else:
print("#Date\t\t\tTime\t\tName\t\tAdults\t\tChildren")
for item in reservation:
f2 = open("reservation.txt", "r")
print("Records are:")
print(f2.read())
f2.close()
elif(choice =="b"):
try:
rnum += 1
name = input("Enter Name: ")
Date = input("Enter date(DD-MM-YYYY): ")
Time = input("Enter time(HH:MM): ")
adults = input("Number of adults: ")
Children = input("Number os children: ")
f1.write (str(rnum))
f1.write("\t")
f1.write(Date)
f1.write("\t")
f1.write(Time)
f1.write("\t\t")
f1.write(name)
f1.write("\t\t")
f1.write(adults)
f1.write("\t\t")
f1.write(Children)
f1.write("\t")
total = int(adults)*500 + int(Children)*300
reservation[rnum]= [Date,Time,name,adults,Children,total]
f1.write(str(total))
f1.write("\n")
f1.close()

print("\nBelow are your Reservation Details:")
print(
f"Reservation Number\t\t{rnum}\nName\t\t{name}\nDate\t\t{Date}\nTime\t\t\{Time}\nTotal Adults\t\t{adults}\nTotal children\t\t{Children}\n")
print(reservation)

except ValueError:
print("there is an incorrect value!! try again")


elif(choice == "c"):
getindex = 0;
rnumd = int(input("Enter Reservation number:"))
try:
reservation.pop(rnumd)
except KeyError:
print("Invalid reservation ID")

print("Reservation deleted")

elif(choice == "d"):
print("#Date\t\t\tTime\t\tName\t\tAdults\t\tChildren\tSubtotal")
for item in reservation:
for i in reservation.get(item):
print(f"{i}",end="\t\t")
print("\n")
elif(choice == "e"):
break

try:
    rnum += 1
name = input("Enter Name: ")
Date = input("Enter date(DD-MM-YYYY): ")
Time = input("Enter time(HH:MM): ")
adults = input("Number of adults: ")
Children = input("Number os children: ")
f1.write(str(rnum))
f1.write("\t")
f1.write(Date)
f1.write("\t")
f1.write(Time)
f1.write("\t\t")
f1.write(name)
f1.write("\t\t")
f1.write(adults)
f1.write("\t\t")
f1.write(Children)
f1.write("\t")
total = int(adults) * 500 + int(Children) * 300
reservation[rnum] = [Date, Time, name, adults, Children, total]
f1.write(str(total))
f1.write("\n")
f1.close()

print("\nBelow are your Reservation Details:")
print(
    f"Reservation Number\t\t{rnum}\nName\t\t{name}\nDate\t\t{Date}\nTime\t\t\{Time}\nTotal Adults\t\t{adults}\nTotal children\t\t{Children}\n")
print(reservation)

except ValueError:
print("there is an incorrect value!! try again")

try:
    reservationNumber += 1
    name = str(input('Enter Name: '))
    date = str(input('Enter Date: '))
    time = str(input(('Enter Time: '))
    adults = int(input('Enter No. of Adults: ')
    children = int(input('Enter No. of Children: ')
    total = adults * 500 + Children * 300
    t_adult.append(adults)
    t_child.append(adults)
    o_total.append(total)
    reservation[rnum] = [Date, Time, name, adults, Children, total]

    print("\nBelow are your Reservation Details:")
    print(
        f"Reservation Number\t\t{rnum}\nName\t\t{name}\nDate\t\t{Date}\nTime\t\t{Time}\nTotal Adults\t\t{adults}\nTotal children\t\t{Children}\n")
    print(reservation)

    rev = Reservation(name, date, time, adults, children)
    r1 = rev.showReservation()
    file = open("reservation.txt", "a")
    file.write(str(r1))
    file.close()
    print('File has been updated.\n')

    # for r in reservation:
    #     rDetails = reservation.get(r)
    #     lDetails = list(rDetails)
    #     print(lDetails[:-1])