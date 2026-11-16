#Arionsae McCutcheo
# This script tests various numeric conversion techniques.

a = "  101.1 " 
b = '55' 
c = "402 Stevens" 
d = 'Number 5 '

new_c = c[0:3] #402
new_d = d[7:8] #5
print (f"{a}".strip)
print (f"{d}".strip)
int (a) #ValueError: invalid literal for int() with base 10: '  101.1 '
int (b) #ValueError: invalid literal for int() with base 10: '  101.1 '
int (c) # ValueError: invalid literal for int() with base 10: '402 Stevens'
int (d) # ValueError: invalid literal for int() with base 10: 'Number 5 '

float (a) # 101.1
float (b) # 55.0
float (c) # ValueError: could not convert string to float: '402 Stevens'
float (d) # ValueError: could not convert string to float: 'Number 5

int (float(a)) # 101
int (float(b)) # 55
int (float(c)) # ValueError: could not convert string to float: '402 Stevens'
int (float(d)) # ValueError: could not convert string to float: 'Number 5'

