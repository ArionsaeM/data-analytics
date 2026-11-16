#Arionsae McCutcheon
#3 3. Federal taxes are 23% of your salary every month. You make X amount of money. 
# How much is withheld for taxes? 

salary = float(input('Enter your monthly salary:')) #ex:$1234.45

taxes_deduction_rate = (1- .77)
tax_deduction_amount = salary * taxes_deduction_rate
print (f'Your tax deduction monthly rate is : {tax_deduction_amount:,.2f}') #ex: output : #$283.92