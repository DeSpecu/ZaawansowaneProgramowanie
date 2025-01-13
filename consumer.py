import csv
import time

def read_tasks(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        tasks = list(reader)
    return tasks

def write_tasks(filename, tasks):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

def consume_task(filename):
    tasks = read_tasks(filename)

    for task in tasks:
        if task[1] == "pending":
            task[1] = "in_progress"
            write_tasks(filename, tasks)
            print(f"Started task {task[0]}: {task[2]}")

            time.sleep(30)

            task[1] = "done"
            write_tasks(filename, tasks)
            print(f"Completed task {task[0]}: {task[2]}")
            return


tasks_file = "tasks.csv"

while True:
    consume_task(tasks_file)
    time.sleep(5)