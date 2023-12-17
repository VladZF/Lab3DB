# Бенчмарк python модулей для работы с базами данных

## Оглавление


  - [Оглавление](#оглавление)
  - [1) Про бенчмарк](#1-про-бенчмарк)
  - [2) Настройка конфига](#2-настройка-конфига)
  - [3) Запуск бенчмарка](#3-запуск-бенчмарка)
  - [4) Реализация '4queries' через данный бенчмарк.](#4-реализация-4queries-через-данный-бенчмарк)
    - [Tiny (200 Mb)](#tiny-200-mb)
    - [Big (2 Gb)](#big-2-gb)
  - [5) Про модули](#5-про-модули)
    - [5.1) Psycopg2](#51-psycopg2)
    - [5.2) Pandas](#52-pandas)
    - [5.3) SQLAlchemy](#53-sqlalchemy)
    - [5.4) SQLite](#54-sqlite)
    - [5.5) DuckDB](#55-duckdb)
  - [6) Выводы](#6-выводы)

## 1) Про бенчмарк

Данный бенчмарк представляет собой замеры времени выполнения запросов в различных python модулях для работы с базами данных. Сейчас для теста доступно пять модулей: Psycopg2, pandas, SQLAlchemy, SQLite и DuckDB. Поведение приложения настраивается с помощью специального файла [config.py](https://github.com/VladZF/Lab3DB/blob/master/config.py).

> [!NOTE]
> Данный бенчмарк не заполняет никакие БД и файлы данными (за исключением времен выполнения запросов). Для работы требуется заранее заполнить базу данных / файл с БД данными. Цель данного проекта - запуск запросов в определенных модулях.

## 2) Настройка конфига

В конфигурационном файле заданы 6 переменных, которые определяют поведение программы в целом.

- DB_PARAMS - данная переменная является python-словарем и содержит в себе параметры для подключения к базе данных. для работы необходимо заполнить пустые значения корректными данными, а вместно ```0``` нужный порт (например ```5432``` для postgresql).

> [!NOTE]
> Требует заполнения для работы с psycopg2, sqlalchemy и pandas

- ATTEMPT_COUNT - количество запусков каждого запроса. Рекомендуемое значение ```20``` для лучшего баланса между точностью среднего времени выполнения запроса и временем работы бенчмарка.

- DATASET - путь к нужному файлу с базой данных (например, путь к .db файлу)

> [!NOTE]
> Требует заполнения для работы с sqlite и pandas

- QUERIES - запросы для тестирования, записанные в виде python-списка в формате ```["""query1""", """query2""", ...]```

- RESULT_FILE_FOLDER - путь к папке, куда будут записываться средние времена выполнения запроса в файл ```results.txt``` в формате
```
<Module> test:
<query 1 time>
<query 2 time>
...
<query 'k' time>
```

- LIB - Python-словарь в формате ```{<module1_name>: True/False, ...}```. True - модуль будет запущен, False - модуль не будет запущен.

## 3) Запуск бенчмарка

После настройки конфигурационного файла, необходимо открыть папку с бенчмарком в консоли и прописать команду ```python main.py```.


## 4) Реализация '4queries' через данный бенчмарк.

Ниже будут приведены замеры с использованием запросов из популярного бенчмарка 4queries, и таблицы trips.

Для того, чтобы реализовать этот тип бенчмарка, нужно ввести следующие запросы:

```python
QUERIES = [
    """SELECT "VendorID", COUNT(*)
        FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", AVG("total_amount")
       FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*)
       FROM trips GROUP BY 1, 2;""",
    """SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
]
```

> [!NOTE]
> Для SQLALchemy, psycopg2 и pandas необходимо заменить ```EXTRACT(year FROM "tpep_pickup_datetime")``` на ```DATE_PART('Year', tpep_pickup_datetime::date)```, а для duckdb и SQLite - на ```STRFTIME('%Y', "tpep_pickup_datetime")```.

Были использованы две версии дата сета:


### Tiny (200 Mb)

|   |   |   |   |   |   |
|---|---|---|---|---|---|
||Pandas|Psycopg2|SQLite|DuckDB|SQLAlchemy|
|Query 1|0,377|0,358|0,948|0,142|0,352|
|Query 2|0,478|0,462|1,644|0,16|0,457|
|Query 3|5,606|5,578|2,791|0,195|5,641|
|Query 4|5,885|5,856|5,708|0,212|6,062|

![Tiny set](https://github.com/VladZF/Lab3DB/blob/master/pictures/TinySet.png)

### Big (2 Gb)

|   |   |   |   |   |   |
|---|---|---|---|---|---|
||Pandas|Psycopg2|SQLite|DuckDB|SQLAlchemy|
|Query 1|3,518|3,522|9,539|1,024|3,417|
|Query 2|4,53|4,578|16,172|1,149|4,434|
|Query 3|21,826|59,805|27,87|1,455|58,324|
|Query 4|60,719|62,599|59,272|1,544|61,265|

![Big set](https://github.com/VladZF/Lab3DB/blob/master/pictures/BigSet.png)

(Время прописано в секундах).

## 5) Про модули

Если говорить в общем, каждая библиотека из рассмотренных имеет место в области анализа данных, все они различаются методами работы, и каждый имеет свои преимущества. Установка модулей не вызывает сложностей.

### 5.1) Psycopg2

Psycopg2 - это библиотека для работы с PostgreSQL в Python. Она предоставляет удобные инструменты для выполнения SQL-запросов, чтения и записи данных, управления транзакциями и загрузки данных из csv-файлов. Однако, стоит отметить, что операции загрузки данных в PostgreSQL могут занимать больше времени по сравнению с SQLite или файлами .db, и скорость работы библиотеки может быть ниже, чем у duckDB. Оптимизация настройки PostgreSQL может значительно улучшить производительность операций. Лично мне понравилось работать с данной библиотекой, так как она очень удобна в использовании, и проявляет неплохую эффективность.

### 5.2) Pandas

Pandas - это библиотека Python для анализа данных, предоставляющая удобные структуры данных (DataFrame) и инструменты для работы с ними. Она обладает широкими возможностями для фильтрации, сортировки, группировки и агрегации данных, обработки пропущенных значений, работы с временными рядами и чтения/записи данных из/в различных форматов. Pandas популярна среди специалистов по анализу данных и научных исследований. По моему мнению, это самая удобная и универсальная из 5 библиотек, которые я рассматривал, для работы с данными и их анализом, так как помимо обработки в собственных структурах, модуль умеет интегрироваться с другими модулями, а также подключаться к сторонним сервисам, по типу postgresql и т.д.

### 5.3) SQLAlchemy

SQLAlchemy - это библиотека на языке Python, которая предоставляет инструменты для работы с базами данных с использованием языка SQL. Она позволяет создавать объектно-реляционные отображения (ORM), которые позволяют работать с данными в базе, используя объекты и методы Python, вместо явного написания SQL-запросов.SQLAlchemy поддерживает различные базы данных, такие как PostgreSQL, MySQL, SQLite, и другие, что делает ее универсальным инструментом для работы с различными СУБД. SQLAlchemy также предоставляет возможности для создания сложных запросов, транзакций, а также миграции схемы базы данных. Благодаря своей гибкости и мощным возможностям, SQLAlchemy широко используется для разработки веб-приложений, анализа данных и других приложений, где требуется взаимодействие с базами данных. В данном бенчмарке SQLAlchemy проявляет средние результаты. По поводу впечатлений не могу сказать ничего такого (скорее всего из-за того, что я использовал не весь потенциал данного модуля и не создавал никаких моделей).

### 5.4) SQLite

SQLite - это легкая и встроенная реляционная база данных, которая не требует отдельного сервера. Она проста в использовании, поддерживает SQL, надежна, поддерживает различные языки программирования и кроссплатформенна. Часто используется в мобильных приложениях, браузерах и встроенных системах. SQLite показывает себя хуже всех на первых двух запросах их '4queries', но довольно неплохо показывает себя на третьем и четвертых запросах, где присутствует ```group by```. Так что, можно сказать, что в отличие от предыдущих трех библиотек, обговоренных выше, SQLite лучше работает с группировкой данных. 

### 5.5) DuckDB

DuckDB - это компактная аналитическая база данных с открытым исходным кодом, разработанная для обработки больших объемов данных. Она оптимизирована для выполнения сложных запросов и аналитических операций на больших наборах данных. DuckDB обеспечивает высокую производительность благодаря инновационным методам обработки запросов и компактному хранению данных. Она поддерживает стандарт SQL и может быть легко интегрирована с различными языками программирования, такими как Python, R, и другими. DuckDB также может использоваться в качестве встроенной базы данных для приложений и аналитических инструментов. В '4queries' данных модуль показал ошеломительно быстрый результат, особенно в большом датасете, где среднее время не превышает двух секунд (!!!) даже на третьем и четвертом запросах. Я считаю, что duckdb - это лучшее решение для работы с огромными потоками данных. По удобству в использовании я бы отдал предпочтение pandas, так он универсальнее и имеет большую поддержку внешних и внутренних структур, а также для работы не требуется установки дополнительных расширений: например, duckdb может попросить установить расширение ```sqlite``` для корректной работы. Это можно сделать следующей коммандой:

```python
duckdb.install_extension("sqlite")
```

## 6) Выводы

В целом, при написании бенчмарка я убедился в том, насколько много путей имеется на данное время анализировать данные и работать с ними. Не даром говорят, что python - лучший язык программирования для data science. Я считаю, что бенчмарк '4queries' очень показателен, так как может показывать, насколько эффективно выполняются запросы в той или иной библиотеке, что может определить ход работы в каком-нибудь проекте, где работа с БД - одна из самых главных частей. По поводу своей реализации я хочу сказать, что она универсальна в плане выбора, в какой библиотеке тестировать запросы, и какие запросы собственно подавать.