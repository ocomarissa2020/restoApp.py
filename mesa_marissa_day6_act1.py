def guide():
    print('First Name (first_name): ', name["first_name"])
    print('Middle Name (middle_name): ', name["middle_name"])
    print('Last Name (last_name): ', name["last_name"],'\n')
def updatedRecord():
    print('\n===Record has been Updated===')
    print('First Name: ',    name.get("first_name"))
    print('Middle Name: ', name.get("middle_name"))
    print('Last Name: ', name.get("last_name"),'\n')
name = {
        "first_name": "",
        "middle_name": "",
        "last_name": ""
        }

print("=====Record Keeping App=====")
option = input('Select Menu\n [A] Add Data\n [B] Delete Data\n [Any Key to Exit]\nSelect: ')

while option.upper() != 'A' or option.upper() != "B":
    if option.upper() == 'A':
        print('\n==========Add Record==========')
        guide()
        key = input('Enter Key: ')
        value = input('Enter Value: ')
        name[key] = value
        updatedRecord()
    elif option.upper() == 'B':
        print('\n==========Delete Record==========')
        guide()
        key = input('Enter Key: ')
        name[key] = ""
        updatedRecord()
    else:
        print('Thank You!')
        break
    option = input('Select Menu\n [A] Add Data\n [B] Delete Data\n [Any Key to Exit]\nSelect: ')




    reservation = Reservation(name,date,time,adults,children)
    r1 = reservation.showReservation()
    file = open("reservation.txt", "a")
    file.write(str(r1))
    file.close()
    print('File has been updated.\n')




class Reservation(object):
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = adults
        self.children = children
    def showReservation(self):
        print(self.name + '\t\t' + self.date + '\t\t',self.time,'\t\t'+ self.adults + '\t\t'+ self.children)