from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class TPCreate(BaseModel):
    judul: str
    subjudul: str
    kategori: str
    tanggalpost: datetime
    deadline: datetime
    deskripsi: str

class TPRead(BaseModel):
    id: UUID
    judul: str
    subjudul: str
    kategori: str
    tanggalpost: datetime
    deadline: datetime
    deskripsi: str

class TPUpdate(BaseModel):
    id: UUID
    judul: str
    subjudul: str
    kategori: str
    tanggalpost: datetime
    deadline: datetime
    deskripsi: str
