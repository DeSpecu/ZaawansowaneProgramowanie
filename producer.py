import csv
import time
import uuid

def create_task():
    task_id = str(uuid.uuid4())
    task_status = "pending"
    task_description = f"Rozmowa z klientem {task_id[:8]}"
    return [task_id, task_status, task_description]

def write_task_to_file(filename):
    task = create_task()
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(task)
    print(f"Zadanie o ID: {task[0]} dodano ze statusem '{task[1]}'")


tasks_file = "tasks.csv"
try:
    write_task_to_file(tasks_file)
except FileExistsError:
    pass