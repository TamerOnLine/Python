task = {}

task['id'] = 0
task['title'] = 'Writ'
task['done'] = False
task['pro'] = ['one', 'tow', 'three', 'fuor']
task['note'] = {'id': 0, 'text': 'Talk abut'}
task['due_date'] = ('Today', 'Tomorrow', 'Data')

task_items = task.items()
print(task_items)

task_keys = task.keys()
print(task_keys)

task_values = task.values()
print(task_values)

print(len(task))

task['on'] = 'Onn'

print(task_items)
print(task_keys)
print(task_values)

print(len(task))






