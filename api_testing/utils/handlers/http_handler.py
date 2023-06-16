# The class should contain methods for GET, POST, PUT, PATCH and DELETE request methods
#
# Specify base_url - https://reqres.in/api as class attribute
#
# Use validator in class methods to validate response data structure

import requests
import json
from ..logger import setup_logging
from ..validator import validator, _load_json_schema


class HTTPHandler:
    base_url = "https://reqres.in/api"

    @staticmethod
    def validate_response(response):
        try:
            response_json = response.json()
            # Ваш код валидации структуры данных в ответе
            # Например, можно проверить наличие определенных полей или их типы
            # Если структура данных не соответствует ожидаемой, можно вызвать исключение
        except json.JSONDecodeError:
            raise Exception("Invalid JSON response")

    @classmethod
    def get(cls, endpoint):
        url = f"{cls.base_url}/{endpoint}"
        response = requests.get(url)
        cls.validate_response(response)
        return response.json()

    @classmethod
    def post(cls, endpoint, data):
        url = f"{cls.base_url}/{endpoint}"
        response = requests.post(url, json=data)
        cls.validate_response(response)
        return response.json()

    @classmethod
    def put(cls, endpoint, data):
        url = f"{cls.base_url}/{endpoint}"
        response = requests.put(url, json=data)
        cls.validate_response(response)
        return response.json()

    @classmethod
    def patch(cls, endpoint, data):
        url = f"{cls.base_url}/{endpoint}"
        response = requests.patch(url, json=data)
        cls.validate_response(response)
        return response.json()

    @classmethod
    def delete(cls, endpoint):
        url = f"{cls.base_url}/{endpoint}"
        response = requests.delete(url)
        cls.validate_response(response)
        return response.json()


handler = HTTPHandler()
response = handler.get("users?page=2")
print(response)

# import allure
# import requests
# from src.logger import Logger
# from data.urls import BASE_URL
#
#
# class MyRequests:
#     @staticmethod
#     def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
#         with allure.step(f"POST request to URL '{url}'"):
#             return MyRequests._send(url, data, headers, cookies, "POST")
#
#     @staticmethod
#     def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
#         with allure.step(f"GET request to URL '{url}'"):
#             return MyRequests._send(url, data, headers, cookies, "GET")
#
#     @staticmethod
#     def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
#         with allure.step(f"PUT request to URL '{url}'"):
#             return MyRequests._send(url, data, headers, cookies, "PUT")
#
#     @staticmethod
#     def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
#         with allure.step(f"DELETE request to URL '{url}'"):
#             return MyRequests._send(url, data, headers, cookies, "DELETE")
#
#     @staticmethod
#     def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
#         url = f"""{BASE_URL}{url}"""
#
#         if headers is None:
#             headers = {}
#         if cookies is None:
#             cookies = {}
#
#         Logger.add_request(url, data, headers, cookies, method)
#
#         if method == "GET":
#             response = requests.get(url, params=data, headers=headers, cookies=cookies)
#         elif method == "POST":
#             response = requests.post(url, data=data, headers=headers, cookies=cookies)
#         elif method == "PUT":
#             response = requests.put(url, data=data, headers=headers, cookies=cookies)
#         elif method == "DELETE":
#             response = requests.delete(url, data=data, headers=headers, cookies=cookies)
#         else:
#             raise Exception(f"""Bad method '{method}' was received""")
#
#         Logger.add_response(response)
#
#         return response