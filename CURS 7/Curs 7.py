from traceback import print_tb

employees = ['Michal', 'Harry', 'Susan', 'Dan', 'Christen']
email = ['michal@comp.com', 'harryf@comp.com', 'susan@comp.com', 'dan2@comp.com', 'chris@comp.com']

employees_details = {}

for i in range(len(employees)):
    employees_details[employees[i]] = email[i]

print(employees_details)