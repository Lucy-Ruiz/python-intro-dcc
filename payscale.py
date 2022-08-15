pay_rate = float(input("Please enter your pay rate: "))
hours_worked_per_week = float(input("Please enter your hours worked: "))
total_pay = 0
standard_work_week = 40

#overtime
overtime_multiplier = 1.5

#taxes
income_tax = 0.30

#pto
total_pto_yearly = 12
hours_per_day = 8
yearly_pto_hours = total_pto_yearly * hours_per_day
weeks = 52
weekly_pto_cumulative = yearly_pto_hours / weeks


if hours_worked_per_week > standard_work_week:
    #calc overtime pay
    regular_pay = pay_rate * standard_work_week
    hours_of_overtime = hours_worked_per_week - standard_work_week
    pay_rate_on_overtime = pay_rate * overtime_multiplier
    overtime_pay = hours_of_overtime * pay_rate_on_overtime
    gross_income = overtime_pay + regular_pay
    taxes = gross_income * income_tax
    net_income = gross_income - taxes
    standard_pto = (standard_work_week * weekly_pto_cumulative) / standard_work_week
    
else:
    gross_income = pay_rate * hours_worked_per_week
    taxes = gross_income * income_tax
    net_income = gross_income - taxes
    standard_pto = (hours_worked_per_week * weekly_pto_cumulative) / standard_work_week
print(net_income)