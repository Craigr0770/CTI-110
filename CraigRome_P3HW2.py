#Rome Craig
#10/26/23
#Use if /else statments
# get name and hours workerd from user
# get pay rate
#get overtime
#get reg hours.



name = input("Enter your name : ")

HR = float(input('Enter your hours worked this week : '))

PR = float(input("Enter your pay rate : "))


"""

"""


OT = 0
if HR > 40:
    OT = HR - 40
    RG = HR - OT
else:
    OT = 0
    RG = HR



Pay = RG * PR

OTP = (OT * PR) * 1.5

GP = OTP + Pay



print("--------------------------------------------")

print("Employee name:  " , name)

print()

print("Hours Worked   Pay rate   Overtime rate   OverTime Pay     RegHour Pay     Gross Pay")

print("-----------------------------------------------------------------------------------------")
print(f"{HR}             {PR}         {OT}          {OTP}            {Pay}          {GP}")
