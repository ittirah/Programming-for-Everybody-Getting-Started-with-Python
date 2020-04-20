# Write a program to prompt the user for hours and rate
# per hour using raw_input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5
# times the hourly rate for all hours worked above 40
# hours.

# Use 45 hours and a rate of 10.50 per hour to test
# the program (the pay should be 498.75).
# You should use raw_input to read a string and
# float() to convert the string to a number.
# Do not worry about error checking the user input -
# assume the user types numbers properly.

# Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
# 475 = 40 * 10 + 5 * 15

# Enter Hours: 45
# Enter Rate: 10.50
# Pay: 498.75

hours = float(input('Enter the hours worked'))
rate = float(input('Enter the rate per hour'))

if (0 <= hours) and (hours <= 40) :
    pay = hours * rate
elif hours > 40:
    pay = 40*rate + (hours - 40)*1.5*rate

print('Pay: ',pay)
