#  UsersTestSelemium

### Описание

Цель проекта: получение навыков в написание автоматизированных тестов на Python
и написание API запросов для Postman на примере веб-сайта (<a href="http://users.bugred.ru/">users</a>).

## Технологии

- Python 3.10.9
- Selenium
- PyTest
- PyTest-html
- request
- Postman

## Состав проекта

- Файлы (tests_selenium) с Python тестами
- Файлы (tests_api_python) с Python API тестами
- Файлы (test_api_postman) с API тестами 
- Файлы (test_case) с тест кейсами к API тестам (Selenium)
- Файлы (test_list) с тест листами к API тестам (Selenium)

## Окружение

## Запуск тестов

## Selenium тесты

Пример запуска Selenium тестов:
Для запуска тестов надо ввести следующую команду:<br>
<b>py.test --alluredir=allure_report tests_selenium</b><br>
Для просмотра отчёта:<br>
<b>allure serve allure_report</b>

<img src="img/TestsSelenium.png" width="700" height="400">

## Python API тесты

Пример запуска API тестов:

<img src="img/TestsPythonAPI.png" width="700" height="400">

## Report Selenium Allure

<img src="img/SeleniumReportAllure.png" width="700" height="400">

## Report Selenium

<img src="img/SeleniumReport.png" width="700" height="400">

## Postman

Пример запуска тестов в Postman:

<img src="img/TestsPostmanAPI.png" width="700" height="400">

## Report Postman

<img src="img/PostmanReport.png" width="700" height="400">

## Test Case

Пример тест кейсов для API запросов Postman:

<img src="img/TestsCaseUsersAPI.png" width="700" height="400">

## Test List

Пример тест листов для API запросов Postman:

<img src="img/TestsListUsersAPI.png" width="700" height="400">

## Будущие изменения

- [X] Сделать фикстуру удаления пользователя
- [X] Сделать фикстуру выхода пользователя из аккаунат
- [X] Добавить API python тесты
- [X] Добавить API test list
- [X] Добавить Reports
- [X] Добавить Allure отчёты
