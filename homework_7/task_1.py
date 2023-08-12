"""
 Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени.
    Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
    К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

Пример:
rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
foto_2002.txt -> o_20video001.csv
"""
from os import listdir, path, rename, chdir


def rename_files(wanted_name: str, count_nums: int, extension_old: str, extension_new: str, diapazon: list) -> None:
    count = 1
    chdir('test')
    list_files = listdir()
    for file in list_files:
        if path.isfile(file):
            if ('.' + file.split('.')[1]) == extension_old:
                old_name = file[diapazon[0]:diapazon[1]]
                rename(file, f'{old_name}{wanted_name}{str(10 ** count_nums + count)[1::]}{extension_new}')
                count += 1
    print(f'Изменено {count-1} файлa(-ов). \nПрограмма завершена.')


rename_files(wanted_name='video', count_nums=3, extension_old='.txt', extension_new='.xml', diapazon=[2, 6])
