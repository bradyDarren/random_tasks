import random

assignment = ["Project Management", "Data Analysis", "Customer Support", "Marketing Campaign", 
    "Software Development", "Product Design", "Technical Writing", "Sales Outreach", 
    "Quality Assurance", "Human Resources Training", "Financial Auditing", "Client Presentation"]

employees = ["John Smith", "Jane Doe", "Michael Johnson", "Emily Davis", "Robert Wilson", 
    "Linda Martinez", "James Brown", "Patricia Taylor", "David Anderson", 
    "Barbara Moore", "Richard Thomas", "Jessica Harris", "Charles White", 
    "Susan Clark", "Joseph Lewis", "Sarah Lee", "Daniel Walker", "Karen Hall"]

# prompting the user to input the assignments needed to be distributed
# user_assignment = input("Input the tasks needed to be assigned. Please seperate by a comma. : ")

# for task in user_assignment.split(","):
#     assignment.append(task.strip())
# print(assignment)

# # prompting the user to input the employes that assignments can be distributed to.
# # user_employees = input("Input the name of the employees needed to be assigned. Please seperate by a comma. : ")

# for emp in user_employees.split(","):
#     employees.append(emp.strip())

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

    


