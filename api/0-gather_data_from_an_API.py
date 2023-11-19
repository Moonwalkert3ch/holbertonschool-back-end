#!/usr/bin/python3
""" Write a Python script that, using this 
REST API, for a given employee ID, returns information about 
his/her TODO list progress
"""
import requests
import sys


def main():
    """ returns information about his/her TODO list progress
    Args: Param-emp_id - must be an int, ids employee
    Returns: display data
    """
    employee_id = sys.argv[1]
    response_emp_user = requests.get("https://jsonplaceholder.typicode.com/users")
    response_emp_todo = requests.get("https://jsonplaceholder.typicode.com/todos")

    employee_user = response_emp_user.json()
    employee_todo = response_emp_todo.json()
    employee_name = employee_user.get("name")
    DONE_TASKS = [task.get("title")
                             for task in employee_todo if task.get("completed") is True]
    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          len(DONE_TASKS),
                                                          len(TOTAL_NUMBER_OF_TASKS)))
    print('\n'.join('\t {}'.format(task) for task in tasks))

    #for user in employee_user:
        #if user["id"] == employee_id:
            #employee_name = user["name"]
            #break

    #DONE_TASKS = 0
    #NUMBER_OF_DONE_TASKS = 0

    #TOTAL_NUMBER_OF_TASKS = []

    #for task in employee_todo:
        #if task["userId"] == int(employee_id):
"""
DONE_TASKS += 1
if task["completed"] is True:
NUMBER_OF_DONE_TASKS +=1
TOTAL_NUMBER_OF_TASKS.append(task["title"])

    print(f"Employee {employee_name} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    
    for task in DONE_TASKS:
        print(f"\t{task['title']}")
        """
elif:
    print(f"Error: Failed to retrieve TODO list for employee ID.")

