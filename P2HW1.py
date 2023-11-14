#Rome Craig
#10/5/23
#Into into dictionary.

#user input
name = input("Enter your name: ")
hair = input("Enter your hair color: ")
eye = input ("Enter your eye color: ")
height = float(input("Enter hieght in decimal format: "))
age = int(input("Enter your age: "))
food = input("Whats your favorite food? ")
          #create dictionary
          
#C stands for color
user_traits = {"Name": name,"HairC": hair,"EyeC":eye, 
               "Height":height,"Age":age,"Food":food}


print(f"{user_traits['Name']} is a {user_traits['Height']} tall student with {user_traits['HairC']} hair and {user_traits['EyeC']} eyes. They are {user_traits['Age']} years old and their favorite food is {user_traits['Food']}")
