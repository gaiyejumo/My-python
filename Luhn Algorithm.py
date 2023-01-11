# The codes below shows the luhn algorithm how is runs as a single program and how it runs in a function
card_number = input("Write out your credit card number: ")

sum = 0
num_digits = len(card_number)
oddeven = num_digits & 1
# Ensuring that only positive numbers from 0 the total number of card number
for count in range(0, num_digits):
    digit = int(card_number[count])

    if not (( count & 1 ) ^ oddeven ):
        digit = digit * 2
        print("You number is incomplete")

    if  digit > 9:
        digit = digit - 9
        sum += digit

print ((sum % 10) == 0)

"""
def My_Luhn_Algorithm(card_number):
   #Defines a function that checks credit cards

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    # Ensuring that only positive numbers from 0 the total number of card number
    
    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
            print("You number is incomplete")
        
        if digit > 9:
            digit = digit - 9

        sum += digit

    return ((sum % 10) == 0)
"""