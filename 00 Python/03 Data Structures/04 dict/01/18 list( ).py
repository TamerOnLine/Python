task = {}

task['id'] = 0
task['title'] = 'Writ'
task['done'] = False
task['pro'] = ['one', 'tow', 'three', 'fuor']
task['note'] = {'id': 0, 'text': 'Talk abut'}
task['due_date'] = ('Today', 'Tomorrow', 'Data')

task_items = task.items()
#print(task_items)

task_keys = task.keys()
#print(task_keys)

task_values = task.values()
#print(task_values)




task['on'] = 'Onn'

print(list(task))
print(len(task))


print(list(task_items))
print(list(task_keys))
print(list(task_values))






