user_input = (input("please input a string including , "))

letter_number = 0
commas = 0

letter_number = len(user_input)
commas = user_input.count(",")

print(letter_number)
print(commas)