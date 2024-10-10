import random

assignment = []
employees = []

# prompting the user to input the assignments needed to be distributed
user_assignment = input("Input the tasks needed to be assigned. Please seperate by a comma. : ")

for task in user_assignment.split(","):
    assignment.append(task.strip())
print(assignment)

# prompting the user to input the employes that assignments can be distributed to.
user_employees = input("Input the name of the employees needed to be assigned. Please seperate by a comma. : ")

for emp in user_employees.split(","):
    employees.append(emp.strip())

while employees or assignment:
    if employees == []:
        print(f"There aren't enough people to complete the remaininging tasks ---> {", ".join(assignment)}")
        break
    elif assignment == []:
        print(f"There aren't enough assignments to accomodate the remaining employees ---> {", ".join(employees)}")
        break

    rand_emp = random.choice(employees)
    rand_assign = random.choice(assignment)
    print(f"{rand_emp} ------> {rand_assign}")
    employees.remove(rand_emp)
    assignment.remove(rand_assign)

    


