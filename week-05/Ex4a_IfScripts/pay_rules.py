#Arionsae McCutcheon
#Ex4A- Lab 2 Pay_rules

pay_rate = float(input ('What is your pay rate?'))

hours_worked = float(input('How many hours did you work?'))
gross_pay = pay_rate * hours_worked
if hours_worked>40:
    pay_rate = (pay_rate*1.5)
    print (f'Your Gross Pay is {gross_pay:,.2f} because you worked over 40 hours.')
elif hours_worked < 40:
    pay_rate == pay_rate
    print (f'Your Gross Pay is {gross_pay:,.2f} because you worked under 40 hours.')
else:
    print (f'Your Gross Pay is {gross_pay:,.2f} because you worked exactly 40 hours.')
