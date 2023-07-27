# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}


def zip_in_dict(res=1, reverse=[1, 2, 3]) -> dict:
    local_param = locals()
    param_in_dict = {}
    for key, value in local_param.items():
        try:
            hash(value)
        except TypeError:
            value = f'{value}'
        param_in_dict[value] = key
    return param_in_dict


print(f'Итоговый словарь: {zip_in_dict()}')
