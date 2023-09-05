emp_data = [
    {"Employee ID": "161E90", "Name": "gaurang", "Age": 19, "Salary": 900000},
    {"Employee ID": "161F91", "Name": "nidhish", "Age": 18, "Salary": 200000},
    {"Employee ID": "161F99", "Name": "vishnu", "Age": 19, "Salary": 801090},
    {"Employee ID": "171E20", "Name": "aryan", "Age": 17, "Salary": 2100},
    {"Employee ID": "171G30", "Name": "anmol", "Age": 20, "Salary": 67450},
]
def sorting_emp_data(choice):
    if choice == 1:  
        sorted_data = sorted(emp_data, key=lambda x: x["Age"])
    elif choice == 2:
        sorted_data = sorted(emp_data, key=lambda x: x["Name"])
    elif choice == 3: 
        sorted_data = sorted(emp_data, key=lambda x: x["Salary"])
    else:
        print("Invalid choice. Please select a valid sorting parameter (1, 2, or 3).")
        return


    print("\nSorted Employee Data:")
    print("Employee ID\tName\tAge\tSalary")
    for employee in sorted_data:
        print(
            f"{employee['Employee ID']}\t{employee['Name']}\t{employee['Age']}\t{employee['Salary']}"
        )


print("Sort Employee Data:")
print("1. Age")
print("2. Name")
print("3. Salary")
choice = int(input("Enter option 1/2/3: "))

sorting_emp_data(choice)