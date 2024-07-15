
employee_name = input('Enter name of employee: ')

hours_worked = float(input('Enter number of hours worked this week: '))

pay_rate = float(input("Enter employee's pay rate per hour: "))

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
else:
    regular_hours = hours_worked
    overtime_hours = 0

overtime_pay = 0
if overtime_hours > 0:
    overtime_pay = overtime_hours * (pay_rate * 1.5)

regular_pay = regular_hours * pay_rate

gross_pay = regular_pay + overtime_pay

print(f'{"Hours Worked":<15} {"Pay Rate":<15} {"OverTime":<15} {"OverTime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')
print('-' * 100)
print(f'{hours_worked:<15.2f} ${pay_rate:<14.2f} {overtime_hours:<14.2f} ${overtime_pay:<14.2f} ${regular_pay:<14.2f} ${gross_pay:<14.2f}')
