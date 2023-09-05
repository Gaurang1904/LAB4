import sys

# Create a list of employee data
employee_data = [
    ["161E90", "Raman", 41, 56000],
    ["161F91", "Himadri", 38, 67500],
    ["161F99", "Jaya", 51, 82100],
    ["171E20", "Tejas", 30, 55000],
    ["171G30", "Ajay", 45, 44000],
]


def search_employee_data(search_parameter, search_value):
    """
    Search employee data based on the search parameter and search value.

    Args:
        search_parameter: The search parameter, which can be "age", "name", or "salary".
        search_value: The search value.

    Returns:
        A list of employee data that matches the search criteria.
    """
    matching_employees = []

    for employee in employee_data:
        if search_parameter == "age":
            if employee[2] == search_value:
                matching_employees.append(employee)
        elif search_parameter == "name":
            if employee[1].lower() == search_value.lower():
                matching_employees.append(employee)
        elif search_parameter == "salary":
            if employee[3] == search_value:
                matching_employees.append(employee)
        else:
            print("Invalid search parameter.")
            sys.exit()

    return matching_employees


def print_employee_data(employee_data):
    """
    Print the employee data in a tabular format.

    Args:
        employee_data: The list of employee data to print.
    """
    print("+------+------+------+------+")
    print("| ID    | Name  | Age   | Salary |")
    print("+------+------+------+------+")

    for employee in employee_data:
        print(
            "| {:<7} | {:<8} | {:<6} | {:>8} |".format(
                employee[0], employee[1], employee[2], employee[3]
            )
        )

    print("+------+------+------+------+")


def main():
    """
    Main function.
    """

    print("Employee Table")
    print("Employee ID Name Age Salary (PM)")

    # Get the search parameter from the user
    search_parameter = input("Enter the search parameter (age, name, salary): ")

    # Get the search value from the user
    search_value = input("Enter the search value: ")

    # Search the employee data
    matching_employees = search_employee_data(search_parameter, search_value)

    # Print the matching employee data
    if matching_employees:
        print_employee_data(matching_employees)
    else:
        print("No matching employee data found.")


if __name__ == "__main__":
    main()
