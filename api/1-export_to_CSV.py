#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import sys
import requests
import csv


if __name__ == "__main__":
    url = (f"https://jsonplaceholder.typicode.com/users/")
    employee_user_url = requests.get(url)
    employee_user = employee_user_url.json()

    todo_url = (f"https://jsonplaceholder.typicode.com/users/"
                f"{sys.argv[1]}/todos")
    employee_todo_url = requests.get(todo_url)
    employee_todo = employee_todo_url.json()

    for user in employee_user:
        if user['id'] == int(sys.argv[1]):
            employee_name = user['username']

    with open(argv[1] + '.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for tasks in employee_todo:
            data = []
            if tasks['userId'] == int(sys.argv[1]):
                data.append(tasks['userId'])
                data.append(employee_name)
                data.append(tasks['completed'])
                data.append(tasks['title'])
                writer.writerow(data)