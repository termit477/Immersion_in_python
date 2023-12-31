## Разработка скрипта для категоризации пользовательских запросов
***
### Задание:

#### Вам необходимо написать скрипт на языке Python, который будет категоризировать письма, представленные в формате CSV. Вам будет отправлен CSV-файл с перемешанными обезличенными письмами из разделов: Security, Refunds, Troubleshooting, Account, Advertising and Collaboration, Limits, Payments, Features.

---

Требования:

1. Вам нужно разработать скрипт, который будет считывать содержимое CSV-файла и категоризировать каждое письмо в соответствии с его содержимым. Категория должна быть определена на основе ключевых слов, содержащихся в тексте письма.
2. Проанализируйте содержимое и выявите зависимости.
3. Создайте словарь с ключевыми словами для каждой категории. 
4. Скрипт должен открывать CSV-файл, считывать каждое письмо и проверять его содержимое на наличие ключевых слов для каждой категории.
5. Письмо должно быть отнесено к одной или нескольким категориям, если оно содержит соответствующие ключевые слова и корни к ним. 
6. Результаты категоризации должны быть сохранены в новом CSV-файле или выведены на экран в удобочитаемом формате.
7. Обратите внимание, что ключевые слова могут быть регистронезависимыми, то есть их наличие в письме должно быть определено без учета регистра.
8. Дополнительным плюсом будет реализация обработки исключений, чтобы скрипт не завершался с ошибкой при некорректной структуре CSV-файла или отсутствии файла.
