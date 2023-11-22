#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""

import json
import requests

def export_todo_all_employees():
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    todo = {
        user.get("id"): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            }
            for task in requests.get(url + "todos", params={"userId": user.get("id")}).json()
        ]
        for user in users
    }

    with open("todo_all_employees.json", "w") as f:
        json.dump(todo, f)

if __name__ == "__main__":
    export_todo_all_employees()
