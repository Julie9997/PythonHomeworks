from datetime import datetime
from os.path import exists, join

COLUMNS = ('Время', 'ID Пользователя', 'Пользователь', 'Ввод', 'Результат')

def log(user_id, username, data, result):
    time = datetime.now()
    user_id = str(user_id)
    result = str(result)

    path = "Homework10/log.csv"

    if not exists(path):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(', '.join(COLUMNS) + '\n')
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'{time}, {user_id}, {username}, {data}, {result}\n')
