#Arionsae McCutcheon


pay_rate = float (input ('What is your hourly  pay rate?'))

hours_worked = float(input('How many hours did you work?'))

weekly_gross = pay_rate * hours_worked
print (f' You worked {hours_worked} this period.')
print (f'Because you earn ${pay_rate} per hour, your gross weekly pay is $ {weekly_gross}.')

annual_Gincome = (weekly_gross)* 52

filing_status = input ('Enter your filing status:')
print (f' Your filing status is {filing_status}.')

def single_filers_calc(annual_Gincome):
    tax_rate = 0
    if annual_Gincome < 12000:
        annual_Gincome = annual_Gincome * 1.05

    elif 12000 <= annual_Gincome <= 24999.99:
        annual_Gincome =annual_Gincome*1.10
    elif 25000<= annual_Gincome <= 74999.99:
        annual_Gincome = annual_Gincome * 1.15
    elif annual_Gincome > 75000:
        annual_Gincome = annual_Gincome * 1.20

def joint_filers_calc(annual_Gincome):
    if annual_Gincome < 12000:
        annual_Gincome = annual_Gincome * 1
    elif 12000 <= annual_Gincome <= 24999.99:
        annual_Gincome = annual_Gincome*1.06
    elif 25000<= annual_Gincome <= 74999.99:
        annual_Gincome = annual_Gincome * 1.11
    elif annual_Gincome > 75000:
        annual_Gincome = annual_Gincome * 1.20



if filing_status == "single":
    single_filers_calc()
elif filing_status == "joint":
    joint_filers_calc()