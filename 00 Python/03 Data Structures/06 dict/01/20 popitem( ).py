task = {}

task['id'] = 0
task['title'] = 'Writ'
task['done'] = False
task['pro'] = ['one', 'tow', 'three', 'fuor']
task['note'] = {'id': 0, 'text': 'Talk abut'}
task['due_date'] = ('Today', 'Tomorrow', 'Data')

task_items = task.items()


task_keys = task.keys()


task_values = task.values()





print(task)
print(len(task))
print(task.popitem())
print(task)
print(len(task))








