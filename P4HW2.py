#Rome Craig
#11/2/2023
#



Empn = input("Enter employee's name or Done to terminate : ")


num1 = 0

TOT = 0

TPay = 0

TGP = 0

while Empn != "Done":


    num1 = num1 + 1

    HR = float(input("How many hours worked this week : "))

    PR = float(input("Enter your pay rate : "))

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

    print("Employee name:  " , Empn)

    print()

    print("Hours Worked   Pay rate   Overtime rate   OverTime Pay     RegHour Pay     Gross Pay")

    print("-----------------------------------------------------------------------------------------")

    print(f"{HR}             {PR}         {OT}          {OTP}            {Pay}          {GP}")

    Empn = input("Enter employee's name or Done to terminate : ")

    TOT += OT
    TPay += Pay
    TGP += GP

print(f"the number of employees enter is : {num1}")
print(f"Total amount paid for overtime : {TOT}")
print(f"Total amount paid for regular hours : {TPay}")
print(f"Total amount paid in gross : {TGP}")


