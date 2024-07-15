# Stephen Townsend
# 07-06-24
# P4HW1 
# A program that calculates employee's pay rate and over time

def main():
    overtime_total = 0
    regular_pay_total = 0
    gross_pay_total = 0
    num_employees = 0

    while True:
        employee_name = input("\nEnter employee's name or 'Done' to terminate: ")
        if employee_name.lower() == "done":
            break
        
        num_employees += 1
        
        hours_worked = float(input(f"How many hours did {employee_name} work this week: "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate: "))
        
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
        
        overtime_total += overtime_pay
        regular_pay_total += regular_pay
        gross_pay_total += gross_pay

        print(f'Employee Name: {employee_name}')

        print(f'{"Hours Worked":<15} {"Pay Rate":<15} {"OverTime":<15} {"OverTime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')
        print('-' * 100)
        print(f'{hours_worked:<15.2f} ${pay_rate:<14.2f} {overtime_hours:<14.2f} ${overtime_pay:<14.2f} ${regular_pay:<14.2f} ${gross_pay:<14.2f}')

        
   
    print(f'{"Total number of employees entered:":<30} {num_employees}')
    print(f'{"Total amount paid for overtime:":<30} ${overtime_total:.2f}')
    print(f'{"Total amount paid for regular hours:":<30} ${regular_pay_total:.2f}')
    print(f'{"Total amount paid in gross:":<30} ${gross_pay_total:.2f}')

if __name__ == "__main__":
    main()
