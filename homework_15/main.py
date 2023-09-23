import csv
import logging
import pymorphy2

BASE = {'SECURITY': ['пароль', 'безопасность', 'хакер', 'защита', 'доступ'],
        'REFUNDS': ['возврат', 'отмена', 'деньги', 'возмещение', 'плата', 'отписаться'],
        'TROUBLESHOOTING': ['ошибка', 'неполадка', 'проблема', 'сбой', 'не работает',
                            'недоступно', 'медлен', 'производительно', 'баг', 'зависло', 'починить'],
        'ACCOUNT': ['зарегистировался', 'аккаунт', 'автопродление', 'учетная', 'удалить',
                    'подписка', 'регистрация', 'логин', 'профль', 'настройка', 'изменение данных'],
        'ADVERTISING_AND_COLLABORATION': ['реклама', 'партнество', 'сотрудничество', 'продвижение', 'маркетинг'],
        'LIMITS': ['лимит', 'ресурсы', 'ограничение', 'сколько я мог', 'как увеличить количество', 'период'],
        'PAYMENTS': ['платеж', 'оплата', 'биллинг', 'подписка'],
        'FEATURES': ['функции', 'функционал', 'сервис', 'возможность', 'обновлен',
                     'можно ли использовать', 'когда уже можно', 'формат', 'антиплагиат']}


class WorkFile:
    FORMAT = '{levelname:<8}: {asctime}. В модуле "{name}" в строке {lineno:03d} ' \
             'функция "{funcName}()" в {created} секунд записала сообщение: {msg}'

    logging.basicConfig(filename='log.log',
                        filemode='a',
                        encoding='UTF-8',
                        format=FORMAT,
                        style='{',
                        level=logging.ERROR)

    def read_file(name_file: str):
        logger = logging.getLogger(__name__)
        try:
            with open(name_file, 'r', encoding='UTF-8') as file:
                data = csv.reader(file)
                result = sum(data, [])
            return result
        except FileNotFoundError:
            logger.error('Файл не существует')

    def write_file(name_file: str, mess: str):
        logger = logging.getLogger(__name__)
        try:
            with open(name_file, 'a', encoding='UTF-8-sig', newline='\n') as file:
                file_writer = csv.writer(file, delimiter=';')
                file_writer.writerow([mess])
        except TypeError:
            logger.error('Ошибка записи в файл')


def sorted_message(messages: list):
    morph = pymorphy2.MorphAnalyzer()
    while messages:
        message = messages.pop(0).lower()
        for key, value in BASE.items():
            for i in value:
                word = morph.parse(i)[0]
                if (i in message == True) or (
                        (word.inflect({'gent'}).word in message) == True) or (
                        (word.inflect({'datv'}).word in message) == True) or (
                        (word.inflect({'accs'}).word in message) == True) or (
                        (word.inflect({'ablt'}).word in message) == True) or (
                        (word.inflect({'loct'}).word in message) == True):
                    WorkFile.write_file(f'{key}.csv', message)
                    break


if __name__ == '__main__':
    base = WorkFile.read_file('user_support_letters.csv')
    sorted_message(base)
