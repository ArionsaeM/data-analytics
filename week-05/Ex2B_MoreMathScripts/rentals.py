#Arionsae McCutcheon
"""6. There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost 
$250 per day to rent (including the driver’s pay). How many vans do you need? How 
much will it cost to rent vans? What is the cost if you split it per person? 
Code the script in a file named rentals.py 


Test your script with 38 tourists. Now do some separate calculations to check your 
work: 
a) How much money did your script say you had to charge per person?  
b) If you multiply that out, how much did you collect?  
d) Why do you have leftover money? - Because the total cost is slightly less than the amount collected because of rounding.
7. Remember to commit and push your changes when you finish the exercises. 
"""

tourists = int (input ("Enter the amount of tourists: "))
vans = math.ceil(tourists / 15)
rental_cost = vans * 250

print (f'You will need {vans} to transport {tourists}. The total cost of transport per person is ${rental_cost / tourists:.2f}')

# You will need 3 to transport 38. The total cost of transport per person is $19.74 
