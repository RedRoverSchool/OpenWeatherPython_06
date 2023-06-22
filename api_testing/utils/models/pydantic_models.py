"""This file contains models for pydantic JSON validation"""
from __future__ import annotations
from typing import List
from pydantic import (
    BaseModel,
    StrictStr,
    StrictInt,
)


class Models:
    """This is main class, which contain all models"""

    class SingleUser:
        """Model for API response 'single user' 'https://reqres.in/api/users/2'"""

        class Data(BaseModel):
            id: StrictInt
            email: StrictStr
            first_name: StrictStr
            last_name: StrictStr
            avatar: StrictStr

        class Support(BaseModel):
            url: StrictStr
            text: StrictStr

        class Model(BaseModel):
            data: Models.SingleUser.Data
            support: Models.SingleUser.Support

    class SingleUserBroken:
        """Broken Model for API response 'single user' 'https://reqres.in/api/users/2'"""

        class Data(BaseModel):
            id: StrictInt
            email: StrictInt  # suppose to be "StrictStr"
            first_name: StrictStr
            last_name: StrictStr
            avatar: StrictStr

        class Support(BaseModel):
            url: StrictStr
            text: StrictStr

        class Model(BaseModel):
            data: Models.SingleUserBroken.Data
            support: Models.SingleUserBroken.Support

    class ListUsers:
        """Model for API response 'list users' 'https://reqres.in/api/users?page=2'"""

        class Datum(BaseModel):
            id: StrictInt
            email: StrictStr
            first_name: StrictStr
            last_name: StrictStr
            avatar: StrictStr

        class Support(BaseModel):
            url: StrictStr
            text: StrictStr

        class Model(BaseModel):
            page: StrictInt
            per_page: StrictInt
            total: StrictInt
            total_pages: StrictInt
            data: List[Models.ListUsers.Datum]
            support: Models.ListUsers.Support

    class ListUsersBroken:
        """Broken for API response 'list users' 'https://reqres.in/api/users?page=2'"""

        class Datum(BaseModel):
            id: StrictStr  # suppose to be "StrictInt"
            email: StrictStr
            first_name: StrictStr
            last_name: StrictStr
            avatar: StrictStr

        class Support(BaseModel):
            url: StrictStr
            text: StrictStr

        class Model(BaseModel):
            page: StrictInt
            per_page: StrictInt
            total: StrictInt
            total_pages: StrictInt
            data: List[Models.ListUsersBroken.Datum]
            support: Models.ListUsersBroken.Support
