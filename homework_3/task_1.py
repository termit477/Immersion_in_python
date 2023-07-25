# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]


def find_dublicate(list_old: [int]) -> list[int]:
    list_new = []
    for elem in list_old:
        if list_old.count(elem) > 1:
            list_new.append(elem)
    return list(set(list_new))


my_list = [1, 2, 3, 1, 2, 4, 5]
new_list = find_dublicate(my_list)
print(new_list)
