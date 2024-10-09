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
print(employees)

for partners in employees:
    print(f"{random.choice(employees)} ---------> {random.choice(assignment)}")

# Project Management, Data Analysis, Customer Support, Marketing Campaign, Software Development, Product Design, Technical Writing, Sales Outreach, Quality Assurance, Human Resources Training, Financial Auditing, Client Presentation
# John Smith, Jane Doe, Michael Johnson, Emily Davis, Robert Wilson, Linda Martinez, James Brown, Patricia Taylor, David Anderson, Barbara Moore, Richard Thomas, Jessica Harris, Charles White, Susan Clark, Joseph Lewis, Sarah Lee, Daniel Walker, Karen Hall
