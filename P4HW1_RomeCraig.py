#Rome Craig
#10/31/23
#Sorce list

mg = int(input("how many Scores will you enter? "))

grades_list = []

for grade in range(mg) :
         This_g = int(input("Enter a Score: "))

         while This_g < 0 or This_g > 100:
             print("INVALID Score entered!!!!")
             print("Score should be between 0 and 100")
             This_g = int(input("Enter a grade: "))

         grades_list.append(This_g)
         print(f"{This_g} has been added to the list")

for grade in grades_list:
    print(grade)









print("---------------Results---------------")


print("Lowest Score: :", min(grades_list))
print("Highest Score: :", max(grades_list))
print("Sum of Score: :", sum(grades_list))
print("Average Score :", sum(grades_list)/len(grades_list))

print("-------------------------------------")

