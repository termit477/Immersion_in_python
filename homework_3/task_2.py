# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)
# Решил взять аннотацию к книге Бернара Вербера "Танатонавты"

from bs4 import BeautifulSoup
import requests
import pprint
from itertools import islice

SUM_MAX_VALUES_ELEM = 10
SYNTAX = {ord('"'): ord(' '),
          ord('.'): ord(' '),
          ord(','): ord(' '),
          ord('-'): ord(' '),
          ord('?'): ord(' ')}


def text_from_site() -> str:
    url = 'https://obrazovanie-gid.ru/uchitelyam/tanatonavty-bernar-verber-kratkoe-soderzhanie.html'
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    temp = page.find('div', id='insertABlock').find_all('p')
    string = ''
    for string_from_site in temp:
        if string_from_site.text.find('Эти господа') == True:
            string = string_from_site
    string = 'Аннотация к книге "Танатонавты" Бернар Вербер. ' \
             'История про Мишеля Пэнсона и Рауля Разорбак' + str(string)[4:-4:]
    return string


def formatted_string(string: str) -> list[str]:
    change_string = string.translate(SYNTAX)
    words_in_list = change_string.split()
    for i in range(len(words_in_list)):
        words_in_list[i] = words_in_list[i].capitalize()
    return words_in_list


def entry_in_the_dictionary(words_in_list: list[str]) -> dict[str]:
    words_in_dict = {}
    for elem in words_in_list:
        if elem not in words_in_dict.keys():
            words_in_dict[elem.capitalize()] = words_in_list.count(elem)
    return words_in_dict


def sorted_the_dictionary(words_in_dict: dict[str]) -> list[str]:
    return sorted(words_in_dict.items(), key=lambda x: x[1], reverse=True)


def output_of_values(iterable: list[str], n: int):
    pprint.pprint(list(islice(iterable, n)))


text = text_from_site()
list_words = formatted_string(text)
dict_words = entry_in_the_dictionary(list_words)
final_list_words = sorted_the_dictionary(dict_words)
output_of_values(final_list_words, SUM_MAX_VALUES_ELEM)
