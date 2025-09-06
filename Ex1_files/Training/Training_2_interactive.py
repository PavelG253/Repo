rate = input("Please, rate operator's work from 1 to 5: ")
rate_as_number = int(rate)
if (rate_as_number < 1):
    rate_as_number = 1

if (rate_as_number > 5):
    rate_as_number = 5


print(rate_as_number)


feedback = ''

if (rate_as_number == 1):
    feedback = input("Tell us, what do we need to improve: ")
#else:
#    if (rate_as_number == 2):
#        feedback = input ("What would you like to change? ")
elif (rate_as_number == 2):
    feedback = input("What would you like to change? ")
elif (rate_as_number == 3):
    feedback = input("Tell us, what do you want to add: ")
elif (rate_as_number == 4):
    feedback = input("Why not 5 ")
else:
    feedback = input("Thank you! Your feedback is very important for us! ")

print(feedback)

