# Rome Craig
# 10/19/2023
#Fixing syntax errors


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = (float(input('Enter grade for Module 1: ')))
mod_2 = (float(input('Enter grade for Module 2: ')))
mod_3 = (float(input('Enter grade for Module 3: ')))
mod_4 = (float(input('Enter grade for Module 1: ')))
mod_5 = (float(input('Enter grade for Module 5: ')))
mod_6 = (float(input('Enter grade for Module 6: ')))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

print("Lowest Grade: :", min(grades))
print("Highest Grade: :", max(grades))
print("Sum of Grades: :", sum(grades))
print("Average: :", sum(grades)/len(grades))

#break
avg = (sum(grades)/len(grades))

# determine letter grade for average


if avg >= 90:
    print('Your grade is: A')
elif avg >= 89:
    print('Your grade is: B')
elif avg >= 79:
    print('Your grade is: C')
elif avg >= 69:
    print('Your grade is: D')    
else:
    print('Your grade is: F') # TO DO: finish this





