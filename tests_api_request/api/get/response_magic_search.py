from pydantic import BaseModel


class Companies(BaseModel):
    name: str
    id_company: int


class WhyBlock(BaseModel):
    field: str
    value: str


class Results(BaseModel):
    name: str
    email: str
    date: str
    avatar: str
    by_user: str
    companies: list[Companies]
    why_block: list[WhyBlock]
    type: str


class MagicSearchSuccess(BaseModel):
    foundCount: int
    results: list[Results]


class MagicSearchUnsuccess(BaseModel):
    foundCount: int
    results: list
