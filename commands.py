import utilities
def add(name):
    data = utilities.load('tasks.txt')
    data.append(name + "-incomplete" +'\n')
    utilities.save(data, 'tasks.txt')

def delete(name):
    data = utilities.load('tasks.txt')
    for task in data:
        if task.startswith(name):
            data.remove(task)
    utilities.save(data, 'tasks.txt')

def list(st = 'all'):
    data = utilities.load('tasks.txt')
    if st == 'all':
        for task in data:
            print(task.split('\n')[0])
        return
    for task in data:
        if task.endswith(st + '\n'):
            print(task.split('\n')[0])

def update(index, name):
    i = int(index) - 1
    data = utilities.load('tasks.txt')
    if i >= len(data):
        print("Invalid index")
        return
    new = data[i].split('-')
    new[0] = name
    data[i] = '-'.join(new)
    utilities.save(data, 'tasks.txt')

def mark(index, status):
    i = int(index) - 1
    data = utilities.load('tasks.txt')
    if i >= len(data):
        print("Invalid index")
        return
    new = data[i].split('-')
    new[1] = status + '\n'
    data[i] = '-'.join(new)
    utilities.save(data, 'tasks.txt')