
#Rome Craig
#10/5/2023
#Making code that have the product and adverage of 4 numbers on the same line with no deciamls
#making the same code agin but with 3 behid the decimal.

num1 = (float(input("Enter a number: ")))
num2 = (float(input("Enter another number: ")))
num3 = (float(input("Enter a different number: ")))
num4 = (float(input("Gimmie one more number: ")))

product = (num1*num2*num3*num4)

adverage = ((num1+num2+num3+num4)/4 )

print(f"{product:.0f}  {adverage:.0f} ")

print(f"{product:.3f}  {adverage:.3f} ")
