#Arionsae McCutcheon
# dept_converter.py

department_code = int (input('Enter the department code'))

if department_code == 1:
    print ('Your department is Marketing.')
elif department_code == 5:
    print ('Your department is Human Resources ')
elif department_code == 10:
    print ('Your department is Accounting ')
elif department_code == 12:
    print ('Your department is Legal')
elif department_code == 18:
    print ('Your department is IT')
elif department_code == 20:
    print ('Your department code is Customer Relations')


#match case example
department_code = int (input('Enter the department code.'))
match department_code:
    case 1:
        print ('Your department is Marketing.')
    case 5:
        print ('Your department is Human Resources')
    case 10:
        print ('Your department is Accounting')
    case 12:
        print ('Your department is Legal')
    case 18:
        print ('Your department is IT')
    case 20:
        print ('Your department code is Customer Relations')
