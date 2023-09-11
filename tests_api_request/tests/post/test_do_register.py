from enum import Enum

import allure
import pytest
import requests

from tests_api_request.api.post.request_do_register import DoRegisterReq
from tests_api_request.api.post.response_do_register import DoRegisterResSuccess, DoRegisterResUnsuccess
from tests_api_request.resources.csv.reader_csv_file import ReaderCsvFile


class ResponseStructure(Enum):
    STATUS_CODE = 0
    TYPE = 1
    MESSAGE = 2
    NAME = 3
    AVATAR = 4
    BIRTHDAY = 5
    EMAIL = 6
    GENDER = 7
    DATE_START = 8
    HOBBY = 9


@allure.epic('Проверка Post метода (Do Register)')
class TestDoRegister:
    _URL = "http://users.bugred.ru/tasks/rest/doregister"
    _CSV_FILE_PATH_REQ = '/home/turgor/PycharmProjects/UsersTestSelenium/tests_api_request/resources/csv/data/post/do_register/request_do_register.csv'
    _CSV_FILE_PATH_RES = '/home/turgor/PycharmProjects/UsersTestSelenium/tests_api_request/resources/csv/data/post/do_register/response_do_register.csv'

    def check_result(self, response, extended_result):
        if extended_result[ResponseStructure.TYPE.value] == 'success':
            do_register_res = DoRegisterResSuccess(**response.json())
            assert do_register_res.name == extended_result[ResponseStructure.NAME.value]
            assert do_register_res.avatar == extended_result[ResponseStructure.AVATAR.value]
            assert do_register_res.birthday == int(extended_result[ResponseStructure.BIRTHDAY.value])
            assert do_register_res.email == extended_result[ResponseStructure.EMAIL.value]
            assert do_register_res.gender == extended_result[ResponseStructure.GENDER.value]
            assert do_register_res.date_start == int(extended_result[ResponseStructure.DATE_START.value])
            assert do_register_res.hobby == extended_result[ResponseStructure.HOBBY.value]
        elif extended_result[ResponseStructure.TYPE.value] == 'error':
            do_register_res = DoRegisterResUnsuccess(**response.json())
            assert do_register_res.type == extended_result[ResponseStructure.TYPE.value]
            assert do_register_res.message == extended_result[ResponseStructure.MESSAGE.value]
        else:
            raise 'Error satus code!'

    @pytest.mark.parametrize(
        'data_csv',
        ReaderCsvFile.read_two_csv_file(_CSV_FILE_PATH_REQ, _CSV_FILE_PATH_RES)
    )
    def test_do_register(self, data_csv):
        with allure.step('Подготовка данных'):
            data_req_csv, data_res_csv = data_csv
            test_name, email, name, password = data_req_csv
            extended_result = data_res_csv
            request = DoRegisterReq(email=email, name=name, password=password)
        with allure.step('Post запрос'):
            response = requests.post(self._URL, json=request.__dict__)
        with allure.step('Проверка ответа'):
            self.check_result(response, extended_result)
