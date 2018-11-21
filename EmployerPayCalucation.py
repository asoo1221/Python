# week 4 lab solution employee pay calculation
# Oct 18
# EC

# constants
RATES = 0.20
RATEM = 0.23
ALLOW_1 = 25000
ALLOW_2 = 20000


#inputs

print("\t\tWelcome to the Payroll Program")
empId = input("Please enter your employee id: ")
name = input("Please enter your name: ")
address = input("Please enter your address: ")
status = input("Please enter your marital status - s for single , m for married: ")
grossPay = float(input("Please enter your gross pay: "))

# calculations calculate pay by first determining appropriate allowance
if grossPay < 50000:
    allowance = ALLOW_1
else:
    allowance = ALLOW_2

# calculate total tax
if status == "s":
    totalTax = (grossPay - allowance) * RATES
elif status == "m":
    totalTax = (grossPay - allowance) * RATEM
else:
    totalTax = 0
# calculate  netpay
netPay = grossPay - totalTax

# output results
print("\n\t\tPayroll Details for Employee", empId)
print("Id            \t\t:", empId)
print("Name          \t\t:", name)
print("Address       \t\t:", address)
print("Marital status\t\t:", status)
print("For a gross pay of €",grossPay, "your total tax is €",totalTax,"and your netpay is €", netPay)

print("\n\n\t\tSecurity Feature")
password1 = input("Please enter your password: ")
password2 = input("Please re-enter your password: ")

if password1 != password2:            # test if both entries are equal
    print("Incorrect - passwords are not the same")
else:
    print("Passwords match")