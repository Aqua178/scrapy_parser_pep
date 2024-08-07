#### scrapy_parser_pep
## Описание проекта
Проект представляет собой веб-скрапер для получения информации о PEP . Скрипт использует библиотеку scrapy для парсинга информации о PEP с веб-страниц https://www.python.org/dev/peps/. Полученная информация сохраняется в CSV-файл и содержит номер, название и текущий статус каждого PEP.

## Использование
Скопируйте проект, используя команду:
```
git clone https://github.com/Aqua178/scrapy_parser_pep.git
```
Создайте и активируйте виртуальное окружение, используя команду:
```
python -m venv venv
source venv/bin/activate
```
Установите необходимые зависимости, используя команду:
```
pip install -r requirements.txt.
```
Запустите скрипт, используя команду:
```
scrapy crawl pep
```
## Результаты
После завершения работы скрипта, результаты сохраняются в формате CSV в папку results в корневой директории проекта. Файл содержит информацию о номере, названии и текущем статусе каждого PEP, а также общее количество PEP с каждым статусом.

## Используемые технологии:
- Python
- Scrapy

### Author:
[Vladyka Aleksei](https://github.com/aqua178)
