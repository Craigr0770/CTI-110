
#Rome Craig
#10/19/2023
#working with if else statements



is_leap_year = False
   
input_year = int(input("Enter a year : "))

if input_year % 4 == 0:
     
     if input_year % 100 == 0:
          
          if input_year % 400 == 0:
              is_leap_year = True
             
          else:
              is_leap_year = False
     else:
         is_leap_year = True
else:
    is_leap_year = False



if is_leap_year == False:
    print(input_year , "- not a leap year")

else: 
    print(input_year ,  "leap year")
