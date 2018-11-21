"""
question1
Asoo Azad
Week2lab2
28/09/18
"""
fah = 35
c = Celsius = (5/9) * (fah - 32)
c = round(c, 2)
# Fah is for the fahrenheit and C is for Celsius
fah = int(input("Enter your Fah"))
if fah == 35:
    print("Your Answer is")
    print(c)

# else if the input is more than 35, a print error is given
elif fah != 35:
    print("error")
    exit()
