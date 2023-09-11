from pydantic import BaseModel

class DoRegisterReq(BaseModel):
    email: str
    name: str
    password: str
