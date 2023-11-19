#!/usr/bin/python3
""" Write a Python script that, using this 
REST API, for a given employee ID, returns information about 
his/her TODO list progress
"""

import requests
import sys


def employee_todo_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_user_url = requests.get(url)
    empployee_user = employee_user_url.json()
    employee_name = empployee_user.get("name")

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    employee_todo_url = requests.get(todo_url, params={"userId": employee_id})
    employee_todo = employee_todo_url.json()
    
    TOTAL_NUMBER_OF_TASKS = len(employee_todo)
    NUMBER_OF_DONE_TASKS = sum(task["completed"] for task in employee_todo)

    print(f"Employee {employee_name} is done with tasks" 
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}) :")
    print(f"{employee_name}:", end=" ")

    for task in employee_todo:
        if  task["completed"]:
            print(f"\n\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    employee_todo_progress(employee_id)