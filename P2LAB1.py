#Rome Criag
#10/3/2023
#use floats and expression tocalculate gas cost

#create input variables

#calculate gas cost based off of gallons needed and price per gallon

#Calculate for 20miles, 75miles, 500miles.

gas_milage = (float(input("Enter the car's mpg: ")))
gas_cost = (float(input("Enter the gas price: ")))
twenty_miles = (20/gas_milage) * gas_cost
seventy_miles = (75/gas_milage) * gas_cost
fivehundred_miles = (500/gas_milage) * gas_cost
print(f"{twenty_miles:.2f}  {seventy_miles:.2f}  {fivehundred_miles:.2f}") 
