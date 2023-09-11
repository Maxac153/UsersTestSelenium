from enum import Enum

import allure
import pytest
import requests

from tests_api_request.api.delete.response_delete_avatar import DeleteAvatarSuccess, DeleteAvatarUnsuccess
from tests_api_request.resources.csv.reader_csv_file import ReaderCsvFile


class ResponseStructure(Enum):
    STATUS_CODE = 0
    STATUS = 1
    TYPE = 2
    MESSAGE = 3

class TestDeleteAvatar:
    _BASE_URL = 'http://users.bugred.ru/tasks/rest/deleteavatar/?email='
    _CSV_FILE_PATH_REQ = '/home/turgor/PycharmProjects/UsersTestSelenium/tests_api_request/resources/csv/data/delete/delete_avatar/request_delete_avatar.csv'
    _CSV_FILE_PATH_RES = '/home/turgor/PycharmProjects/UsersTestSelenium/tests_api_request/resources/csv/data/delete/delete_avatar/response_delete_avatar.csv'

    def check_result(self, response, extended_result):
        if extended_result[ResponseStructure.TYPE.value] == 'success':
            magic_search = DeleteAvatarSuccess(**response.json())
            assert magic_search.status == extended_result[ResponseStructure.STATUS.value]
        elif extended_result[ResponseStructure.TYPE.value] == 'error':
            magic_search = DeleteAvatarUnsuccess(**response.json())
            assert magic_search.type == extended_result[ResponseStructure.TYPE.value]
            assert magic_search.message == extended_result[ResponseStructure.MESSAGE.value] + ' '
        else:
            raise 'Error satus code!'

    @pytest.mark.parametrize(
        'data_csv',
        ReaderCsvFile.read_two_csv_file(_CSV_FILE_PATH_REQ, _CSV_FILE_PATH_RES)
    )
    def test_do_register(self, data_csv):
        with allure.step('Подготовка данных'):
            data_req_csv, data_res_csv = data_csv
            test_name, email = data_req_csv
            extended_result = data_res_csv
            url = self._BASE_URL + email
        with allure.step('Get запрос'):
            response = requests.delete(url)
        with allure.step('Проверка ответа'):
            self.check_result(response, extended_result)
