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