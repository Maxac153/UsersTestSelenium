from pydantic import BaseModel


class DoRegisterResSuccess(BaseModel):
    name: str
    avatar: str
    password: str
    birthday: int
    email: str
    gender: str
    date_start: int
    hobby: str


class DoRegisterResUnsuccess(BaseModel):
    type: str
    message: str
