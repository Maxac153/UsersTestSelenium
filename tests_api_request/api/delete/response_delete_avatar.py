from pydantic import BaseModel

class DeleteAvatarSuccess(BaseModel):
    status: str

class DeleteAvatarUnsuccess(BaseModel):
    type: str
    message: str
