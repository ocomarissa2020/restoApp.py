print("=====Record Keeping App=====")
option = input('Select Menu\n [A] Add Record\n [B] View Records\n [C] Clear All Records\n [D] Exit\nSelect: ')

while option.upper() != 'A' or option.upper() != "B" or option.upper() != "C" or option.upper() != "D":
    if option.upper() == 'A':
        print('\n==========Add Record==========')
        name = input('Enter Name: ')
        email = input('Email: ')
        address = input('Address: ')
        user_input = ('\nName: '+ name.upper() + '\nEmail: '+email+'\nAddress: '+address)
        print(user_input)
        file = open("file.txt","a")
        file.write(user_input)
        file.close()
        print('File has been updated.\n')
    elif option.upper() == 'B':
        print('\n==========View Records==========')
        file = open("file.txt","r")
        print(file.read())
        file.close()
    elif option.upper() == 'C':
        print('\n==========Clear All Records==========')
        file = open("file.txt", "r+")
        file.truncate(0)
        file.close()
        print('\n==========No Records Found==========')
    else:
        print('Thank You!')
        break
    option = input('Select Menu\n [A] Add Record\n [B] View Records\n [C] Clear All Records\n [D] Exit\nSelect: ')





class Reservation(object):
    def __init__(self, name, date, time, adults, children):
        self.name = name
        self.date = date
        self.time = time
        self.adults = adults
        self.children = children
    def showReservation(self):
        print(self.name + '\t\t' + self.date + '\t\t',self.time,'\t\t'+ self.adults + '\t\t'+ self.children)



