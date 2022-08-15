#Lab-Variables
#age exercise
age = 29
print(f'I am {age} years old.')

#name exercise
first_name = input('First name: ')
last_name = input('Last name: ')
full_name = first_name + ' ' + last_name
print(full_name)
print(f'My first name is {first_name} and my last name is {last_name}, which means my full name is {full_name}')

#temperature converter exercise subtract 32 and multiply by . 5556 (or 5/9).
fahrenheit_temp = float(input('Enter Fahrenheit temperature: '))
fahrenheit_to_celsius = (fahrenheit_temp - 32) * 0.5556
print(f'{fahrenheit_temp} degrees Fahrenheit is {fahrenheit_to_celsius}')

pay_rate = input("Please enter your pay rate: ")
pay_rate_converted = float(pay_rate)
hours_worked = input("Please enter your hours worked: ")
hours_worked_converted = float(hours_worked)
total_pay = 0
standard_work_week = 50
overtime_multiplier = 1.5

if hours_worked_converted > standard_work_week:
    #calc overtime pay
    regular_pay = pay_rate_converted * standard_work_week
    hours_of_overtime = hours_worked_converted - standard_work_week
    pay_rate_on_overtime = pay_rate_converted * overtime_multiplier
    overtime_pay = hours_of_overtime * pay_rate_on_overtime
    total_pay = overtime_pay + regular_pay
else:
    total_pay = pay_rate_converted * hours_worked_converted

print(total_pay)

