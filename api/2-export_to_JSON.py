#!/usr/bin/python3
"""Export data in JSON format."""

import requests
import sys
import json

def export_user_data(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user details
    emp_user = requests.get(url + f"users/{user_id}").json()
    username = emp_user.get("username")

    # Fetch user's todos
    emp_todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write data to JSON file
    with open(f"{user_id}.json", "w") as f:
        json.dump(
            {
                user_id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username
                    } 
                    for task in emp_todos
                ]
            }, 
            f,
            indent=2
        )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2-export_to_JSON.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_user_data(user_id)
