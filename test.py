number = int(input("Enter a number: "))
if number ==0:
    print("The number is zero")
elif number > 0:
    print("The number is positive")
else:
    print("The number is negative")


userOpinoin = input("Want to run loop? (yes/no): ")
startingpoint = 0
endingpoint = 20

if userOpinoin == "yes" | userOpinoin == "Yes"| userOpinoin == "YES" | userOpinoin == "y" | userOpinoin == "Y":
    while startingpoint <= endingpoint:
        print(startingpoint)
        startingpoint += 1 
else:
    print("Thank you for using the program")