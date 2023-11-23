#!/usr/bin/python3
"""Extend your Python script to export data in CSV format"""

import sys
import requests
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    employee_user_url = requests.get(url)
    employee_user = employee_user_url.json()

    todo_url = (f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
                f"/todos")
    employee_todo_url = requests.get(todo_url)
    employee_todo = employee_todo_url.json()

    for user in employee_user:
        if user['id'] == int(sys.argv[1]):
            employee_name = user['username']

    with open(f"{sys.argv[1]}.csv", 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        # Write header row
        writer.writerow(['User ID', 'Username', 'Completed', 'Task Title'])

        for task in employee_todo:
            if task['userId'] == int(sys.argv[1]):
                writer.writerow([
                    task['userId'],
                    employee_name,
                    task['completed'],
                    task['title']
                ])
