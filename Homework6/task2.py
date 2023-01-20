# Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

lst = [12,'sadf',5643]

nums = list(filter(lambda x: type(x) == int, lst))
print(nums, end=' , ')
txt = list(filter(lambda x: type(x) == str, lst))
print(txt)