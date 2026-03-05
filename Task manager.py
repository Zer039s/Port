tasks = []


def displayTasks(all_tasks):
  print('\nTask Manager: ')
  if len(all_tasks) <= 0:
    print('\nYour tasks! ')
  else:
    for index, task in enumerate(all_tasks):
        print(f'{index+1}: {task}')


def newOperation(all_tasks):
 operation = input("Press 'A' to add a new task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")
 if operation == 'A':
   addTask(all_tasks)
 elif operation == 'E':
   editTask(all_tasks)
 elif operation == 'R':
   removeTask(all_tasks)
 elif operation =='F':
   return
 else:
   newOperation(all_tasks)

def editTask(all_tasks):
    task_number = input('Enter the number of the task you want to edit: ')
    new_task = input('Edit task: ')
    all_tasks[int(task_number)-1] = new_task
    print(f'Item {task_number} edited!')

    displayTasks(all_tasks)
    newOperation(all_tasks)

def removeTask(all_tasks):
  task_number = input('Enter the number of the task you want to remove: ')
  all_tasks.remove(all_tasks[int(task_number)-1])
  print(f'\nItem {task_number} removed!' )
  displayTasks(all_tasks)
  newOperation(all_tasks)

def addTask(all_tasks):
 new_task = input('Add a task: ')
 all_tasks.append(new_task)

 displayTasks(all_tasks)
 newOperation(all_tasks)


# Start application
addTask(tasks)
