from pydantic import BaseModel
from typing import Optional, List


class BaseSchool(BaseModel):
    name: str
    kode_provinsi: str
    kode_kab_kota: str
    kode_kecamatan: str
    bentuk: str
    status: str


class School(BaseSchool):
    uuid: str

    class Config:
        orm_mode: True

