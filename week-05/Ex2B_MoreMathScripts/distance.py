 #Arionsae McCutcheon
 #4. How do you calculate the distance between coordinates (x1, y1) and (x2, y2)?

x1 = float(input('Enter x1 coordinate:')) #ex: 
y1 = float(input('Enter y1:'))

x2 = float(input ('Enter x2:'))
y2 = float (input('Enter y2:'))

distance = ((y2 - y1)**2 +(x2 - x1)**2)**0.5

print (f'The distance between the two points is {distance:,.2f}')