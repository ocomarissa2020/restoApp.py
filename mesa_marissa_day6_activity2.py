from NetSalary import *
from SalaryDeduction import *
from GrossSalary import *

print('Salary Calculator')
employeeName = str(input('Enter Employee Name: '))
hours = int(input('Enter number of hours: '))
healthInsurance = float(input('Enter Health Insurance: '))
loan = float(input('Enter Loan/s: '))
rate = int(500)
tax = grossSalary(hours, rate) * 0.12

print('\nPAYSLIP')

print('EMPLOYEE INFORMATION\n')
print('Employee Name: ', employeeName.upper())

print('\n===========GROSS SALARY==================')
print('Rendered Hours: ', hours)
print('Rate: ', rate)
print('Gross Salary: ', float(grossSalary(hours, rate)))
gross = float(grossSalary(hours, rate))

print('\n==========SALARY DEDUCTION===============')
print('Health Insurance: ', healthInsurance)
print('Loan/s: ', loan)
print('Tax: ', tax)
print('Total Deductions: ', salaryDeduction(healthInsurance, loan, tax))
ded = salaryDeduction(healthInsurance, loan, tax)

print('\n=============NET SALARY==================')
print('\nNet Salary: ', "PHP{:,.2f} ".format(netSalary(gross, ded)))
print('\n=========================================')


# Functions
def viewReservation():
    if (len(reservation) == 0):
        print("There are no reservations!")
    else:
        print("#Date\t\t\tTime\t\tName\t\tAdults\t\tChildren")
    for item in reservation:
        file = open("reservation.txt", "r")
    print(f2.read())
    f2.close()
    file = open("file.txt", "a")
    file.write(user_input)
    file.close()
    print('File has been updated.\n')


def makeReservation(reservationNumber=None):


#
#
# def deleteReservation():
#     print('=====Delete Reservation=====')
#     file = open("reservation.txt", "r+")
#     file.truncate(0)
#     file.close()
#     print('\n==========No Records Found==========')
# def generateReport():
#     print('=====Generate Report=====')
#     print()
# def exit():
#     print('Exit Application. Thanks!')


print("=====RESTAURANT RESERVATION SYSTEM=====")
option = input(
    'Menu\n [A] View All Reservation\n [B] Make Reservation\n [C] Delete Reservation\n [D] Generate Report\n [E] Exit\n Select: ')

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
    option = input(
        'Select Menu\n [A] View All Reservation\n [B] Make Reservation\n [C] Delete Reservation\n [D] Generate Report\n [E] Exit\n Select: ')
