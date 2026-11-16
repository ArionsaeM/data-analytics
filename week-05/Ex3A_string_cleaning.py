#Arionsae McCutcheon
#Lab 2 - string cleaning 

name_1 = "PRIYA SHARMA" 
name_2 = "bob NGUYEN" 
name_3 = "LaTonya Williams" 
salary_1 = "$82,500" 
salary_2 = "$74,000"

print(name_1.lower().title())
print(name_2.lower().title())
print(name_3.lower().title())

print (((salary_1.replace("$", ""))))
print (((salary_2.replace("$", ""))))

int (salary_1.replace("$", "").replace(",", "")) #82500
type(int (salary_1.replace("$", "").replace(",", ""))) #<class 'int'>
