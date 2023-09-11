#  UsersTestSelemium

### Описание

Цель проекта: получение навыков в написание автоматизированных тестов на Python
и написание API запросов для Postman на примере веб-сайта (<a href="http://users.bugred.ru/">users</a>).

## Технологии

- Python 3.11.2
- Selenium
- Request
- Pydantic
- PyTest
- Postman
- Allure
- CSV

## Состав проекта

- Файлы (tests_selenium) с Python тестами
- Файлы (tests_api_request) с Python API тестами
- Файлы (test_api_postman) с API тестами 
- Файлы (test_documentation) с тест кейсами и чек листом к API тестам (Selenium)

## Окружение

Перед тем как запускать тесты нужно установить необходимые зависемости<br>
Введите следующую команду (нужно находиться внутри папки проекта):<br>
<b>pip install -r requirements.txt</b><br>

Для запуска Selenium тестов требуется установить <a href="https://github.com/mozilla/geckodriver/releases/">WebDriver</a>,
а также браузер <a href="https://github.com/mozilla/geckodriver/releases/">Firefox</a>

## Запуск тестов

### Selenium

Для запуска Selenium тестов нужно ввести следующую команду</br>
<b>py.test --alluredir=allure_report_selenium tests_selenium</b><br>

Для просмотра результатов тестов</br>
<b>allure serve allure_report_selenium</b>

### API

Для запуска API тестов нужно ввести следующую команду:<br>
<b>py.test --alluredir=allure_report_api tests_api_request/</b><br>

Для просмотра отчёта:<br>
<b>allure serve tests_api_request</b>

## Selenium тесты

Пример запуска Selenium тестов:

<img src="img/TestsSelenium.png" width="700" height="150">

## Python API тесты

Пример запуска API тестов:

<img src="img/TestsPythonAPI.png" width="700" height="150">

## Report Selenium Allure

<img src="img/SeleniumReportAllure.png" width="700" height="400">

## Report API Allure

<img src="img/ApiReportAllure.png" width="700" height="400">

## Postman

Пример запуска тестов в Postman:

<img src="img/TestsPostmanAPI.png" width="700" height="150">

## Report Postman

<img src="img/PostmanReport.png" width="700" height="400">

## Test Case

<img src="img/TestsCaseUsersAPI.png" width="700" height="400">

## Test List

<img src="img/ChecklistUsersAPI.png" width="700" height="450">
