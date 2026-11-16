# EX 6.1_Income_Tax_Calculator_Assignment
# Arionsae Mccutcheon
# 11/16/2026
# Description: Income Tax Calculator



# TODO 2: Define the constant
TAX_RATE = .20
STANDARD_DEDUCTION = 10000 
additional_deduction = 2000


# TODO 3: Display the program title and a divider line 

print( 'Income Tax Calculator')
print ('-' *20)

# TODO 4: Prompt for gross annual income and convert it to a float

gross_income = float (input ('Enter your gross income: '))

# TODO 5: Prompt for the number of dependents and convert it to an int
dependents = int (input ('Enter the number of dependents:'))

# TODO 6: Calculate the dependent deductions and the total deductions


DEPENDENT_DEDUCTION = additional_deduction* dependents

total_deductions = STANDARD_DEDUCTION + DEPENDENT_DEDUCTION

# TODO 7: Calculate the taxable income
taxable_income = gross_income - total_deductions

# TODO 8: Calculate the estimated income tax

estimated_income_tax = taxable_income * TAX_RATE

# TODO 9: Display the income tax summary

print (f'Gross Income: {gross_income:,.2f}')
print (f'Standard Deduction: {STANDARD_DEDUCTION:,.2f}')
print (f'Dependent Deductions: {DEPENDENT_DEDUCTION:,.2f}')
print (f'Total Deductions:{total_deductions:,.2f}')
print (f'Taxable Income: {taxable_income:,.2f}')
print (f'Tax Rate:{TAX_RATE:,.2f}')
print (f'Estimated Income Tax: {estimated_income_tax:,.2f}')


# format according to the picture example & test




# Show: gross income, standard deduction, dependent deductions,
# total deductions, taxable income, tax rate, and estimated income tax.
# Use f-strings and format monetary values with .2f 
# Adding a comma to the format specifier inserts thousands separators. For example, f"${gross_income:,.2f}" displays $150,000.00.

