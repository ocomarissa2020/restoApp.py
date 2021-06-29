# Day 2, Activity 2

employeeName = str(input('Employee Name: '))
hours = int(input('Enter number of hours: '))
sss = int(input('SSS Contribution: '))
philHealth = int(input('Phil Health: '))
otherLoan = int(input('Housing Loan: '))
ratePerHour = int(input('Rate per Hour: '))
grossSalary = ratePerHour * hours
tax = grossSalary * float(.10)
totalDeductions = sss + philHealth + otherLoan + tax
netSalary = grossSalary - totalDeductions

print('\n==========PAYSLIP===============')
print('==========EMPLOYEE INFORMATION==========\n')
print('Employee Name: ', employeeName)
print('Rendered Hours: ', hours)
print('Rate per Hour: ', ratePerHour)
print('Gross Salary: ', float(grossSalary))
print('\n==========DEDUCTIONS===============')
print('SSS: ', sss)
print('PhilHealth: ', philHealth)
print('Other Loan: ', otherLoan)
print('Tax: ', tax)
print('Total Deductions: ', totalDeductions)
print('\nNet Salary: ', "PHP{:,.2f} ".format(netSalary))