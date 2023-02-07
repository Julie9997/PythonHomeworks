def expression(input):
    expr = input.split()
    for i in range(len(expr)):
        if expr[i].isdigit() or '.' in expr[i]:
            expr[i] = float(expr[i])
    return expr

def count_actions(list):
    count = 0
    for i in list:
        if type(i) == str:
            count += 1
    return count

def actions(list):
    list_work = list.copy()
    if '/' in list_work or '*' in list_work:
        for i in range(len(list_work)):
            if list_work[i] == '/':
                tmp = list_work[i - 1] / list_work[i + 1]
                del list_work[i-1 : i+2]
                list_work.insert(i - 1, tmp)
                break
            elif list_work[i] == '*':
                tmp = list_work[i - 1] * list_work[i + 1]
                del list_work[i-1 : i+2]
                list_work.insert(i - 1, tmp)
                break
    else:
        for i in range(len(list_work)):
            if list_work[i] == '+':
                tmp = list_work[i - 1] + list_work[i + 1]
                del list_work[i-1 : i+2]
                list_work.insert(i - 1, tmp)
                break
            elif list_work[i] == '-':
                tmp = list_work[i - 1] - list_work[i + 1]
                del list_work[i-1 : i+2]
                list_work.insert(i - 1, tmp)
                break
    return list_work

def calculating(input):
    list_expr = expression(input)
    count = count_actions(list_expr)
    list_result = list_expr.copy()

    for i in range(count):
        list_result = actions(list_result)
    return round(list_result[0], 2)

