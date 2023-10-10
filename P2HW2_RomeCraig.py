#Rome Craig
#10/10/23
#working with list

#create variables and get user input (6)

#create an empty list

#add variables to list
#have the min max sum adverage in print statement

m1 =  (float(input("Enter grade for Module 1: ")))
m2 =  (float(input("Enter grade for Module 2: ")))
m3 =  (float(input("Enter grade for Module 3: ")))
m4 =  (float(input("Enter grade for Module 4: ")))
m5 =  (float(input("Enter grade for Module 5: ")))
m6 =  (float(input("Enter grade for Module 6: ")))

grades_list = [m1, m2, m3, m4, m5, m6]

print("---------------Results---------------")

print("Lowest Grade: :", min(grades_list))
print("Highest Grade: :", max(grades_list))
print("Sum of Grades: :", sum(grades_list))
print("Average: :", sum(grades_list)/len(grades_list))

print("-------------------------------------")
