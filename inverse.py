
cc_num = input("Pls enter your credit card number here:")
#reverse the credit card number_num = cc_num[::-1]
print(cc_num, "for reverse")

# convert to integer
cc_nun = [int(x) for x in str(cc_num)]
print(cc_num, "for int")

digits = cc_nun

odd_digits = digits[-1::-2]

even_digits = digits[-2::-2]

print(even_digits)
print(odd_digits)

print(digits,"or doubled")

doubled_digits = 0
doubled_digits += sum(odd_digits)

for index in even_digits:
    if index % 2 == 0:
        doubled_digits.append(digits * 2)
    else:
        doubled_digits.append(digits)
print(doubled_digits)

for  index, digits in digits:
    if digit > 9:
        doubled_digits.append(digits - 9)
    else:
        doubled_digits.append(digit)
print(doubled_digits)
doubled_digits = doubled_digits[16:32]
print(doubled_second_digit_list)

 # sum all digits
sum_of_digits = sum(doubled_second_digit_list)
print(sum_of_digits)
 
#return sum_of_digits % 10 == 0
if sum_of_digits % 10 == 0 :
    print("True")
                                         
else:
    print("false")   
#cc_number = 5399830222298182      4960091814396767
