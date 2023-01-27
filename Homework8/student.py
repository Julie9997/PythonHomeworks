import marks as m

def see_marks():
    lastname = input('Введите фамилию: ')
    count = 0
    for sub in m.subjects:
        with open(f'{sub}.txt',  'r', encoding='utf-8') as file:
            lines = file.readlines()
            subcount = 0
            for i in range(len(lines)):
                marks = lines[i].split()
                if lastname.capitalize() == marks[0]:
                    s = ''
                    for i in range(1, len(marks)):
                        s += f' {marks[i]} '
                    print(f'{sub}: {s}', end=" ")
                    print()
                else:
                    subcount += 1
            if subcount == len(lines):
                count += 1
    if count == len(m.subjects):
        print('Такого ученика нет\n')