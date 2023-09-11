from enum import Enum

import allure
import pytest
import requests

from tests_api_request.api.get.response_magic_search import MagicSearchSuccess, MagicSearchUnsuccess
from tests_api_request.resources.csv.reader_csv_file import ReaderCsvFile


class ResponseStructure(Enum):
    TEST_NAME = 0
    STATUS = 1
    FOUND_COUNT = 2
    NAME_USER = 3
    EMAIL = 4
    DATE = 5
    AVATAR = 6
    BY_USER = 7
    NAME_COMPANY = 8
    ID_COMPANY = 9
    FIELD = 10
    VALUE = 11
    TYPE = 12


class TestMagicSearch:
    _BASE_URL = 'http://users.bugred.ru/tasks/rest/magicsearch?query='
    _CSV_FILE_PATH_REQ = 'tests_api_request/resources/csv/data/get/magic_search/request_magic_search.csv'
    _CSV_FILE_PATH_RES = 'tests_api_request/resources/csv/data/get/magic_search/response_magic_search.csv'

    def check_result(self, response, extended_result):
        if extended_result[ResponseStructure.STATUS.value] == 'success':
            magic_search = MagicSearchSuccess(**response.json())
            assert magic_search.foundCount == int(extended_result[ResponseStructure.FOUND_COUNT.value])
            assert magic_search.results[0].name == extended_result[ResponseStructure.NAME_USER.value]
            assert magic_search.results[0].email == extended_result[ResponseStructure.EMAIL.value]
            assert magic_search.results[0].date == extended_result[ResponseStructure.DATE.value]
            assert magic_search.results[0].avatar == extended_result[ResponseStructure.AVATAR.value]
            assert magic_search.results[0].by_user == extended_result[ResponseStructure.BY_USER.value]
            # assert magic_search.results[0].companies[0].name == extended_result[ResponseStructure.NAME_COMPANY.value]
            # assert magic_search.results[0].companies[0].id_company == int(extended_result[ResponseStructure.ID_COMPANY.value])
            assert magic_search.results[0].why_block[0].field == extended_result[ResponseStructure.FIELD.value]
            assert magic_search.results[0].why_block[0].value == extended_result[ResponseStructure.VALUE.value]
            assert magic_search.results[0].type == extended_result[ResponseStructure.TYPE.value]
        elif extended_result[ResponseStructure.STATUS.value] == 'not found':
            magic_search = MagicSearchUnsuccess(**response.json())
            assert magic_search.foundCount == 0
            assert magic_search.results == []
        else:
            raise 'Error satus code!'

    @pytest.mark.parametrize(
        'data_csv',
        ReaderCsvFile.read_two_csv_file(_CSV_FILE_PATH_REQ, _CSV_FILE_PATH_RES)
    )
    def test_do_register(self, data_csv):
        with allure.step('Подготовка данных'):
            data_req_csv, data_res_csv = data_csv
            test_name, query = data_req_csv
            extended_result = data_res_csv
            url = self._BASE_URL + query
        with allure.step('Get запрос'):
            response = requests.get(url)
        with allure.step('Проверка ответа'):
            self.check_result(response, extended_result)
