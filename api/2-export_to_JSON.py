#!/usr/bin/python3
"""export data in the JSON format."""

import requests
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    emp_user = requests.get(url + "users/{}".format(user_id)).json()
    username = emp_user.get("username")
    emp_todos = requests.get(url + "todos", params={"userId": user_id}).json()

with open("{}.json".format(user_id), "w") as f:
    json.dump({user_id: [{"task": tasks.get("title"),
                          "completed": tasks.get("completed"),
                          "username": username} for tasks in 
                          emp_todos]}, f)