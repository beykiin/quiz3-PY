# Show whether a number entered from the keyboard is even or odd.

# number=int(input("Please enter the number: "))
# if number%2==0:
#     print("The number you entered is even.")
# else:
#     print("The number you entered is odd.")

# If the number entered from the keyboard is odd, append the number 5 as a string to its end; if it's even, append the number 125 as a string to its end. For example, if the entered number is 10, it will become 10125, and if the entered number is 11, it will become 11345, then you will take twice this number.

number=int(input("Please enter the number: "))

if number%2==0:
    number=str(number)+"125"
else:
    number=str(number)+"345"

print(int(number)*2)

