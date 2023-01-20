# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

def code(text):
    count = 1
    res_text = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res_text = res_text + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res_text = res_text + str(count) + text[-1]
    return res_text

def encode(text):
    number = ''
    res_text = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            res_text = res_text + text[i] * int(number)
            number = ''
    return res_text

file = open("Homework5/task3.txt", 'r')
text = file.readline()

text1 = code(text)
print(text1)
text2 = encode(text1)
print(text2)