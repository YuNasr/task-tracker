
def load(file_path):
    with open(file_path, 'r') as f:
        data = unNumbering(f.readlines())
    return data

def save(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(numbering(data))

def numbering(data):
    for i in range(len(data)):
        data[i] = f'{i+1} {data[i]}'
    return data

def unNumbering(data):
    new = []
    for line in data:
        line = line.split(' ', 1)[1]
        new.append(line)
    return new