#Rome Craig
#10/31/23
#Use for Loops


# Get user input


num1 = int(input("Enter an integer: "))

num2 = int(input("Enter another integer: "))


if num1 <= num2:
    for item in range (num1, num2 + 1, 5):
        print (item)
else :
    while num1 > num2 :
        num1 = int(input("Enter an integer: "))

        num2 = int(input("Enter another integer: "))
        for item in range (num1, num2 + 1, 5):
                print (item)
            

        
    
