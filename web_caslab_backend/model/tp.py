from db.base_class import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid

class TP(Base):
    __tablename__ = "tp"

    id = Column(UUID(as_uuid = True), primary_key=True, index=True, default=uuid.uuid4)
    judul = Column(String, index=True, nullable=False)
    subjudul = Column(String, index=True, nullable=False)
    kategori = Column(String, index=True, nullable=False)
    tanggalpost = Column(TIMESTAMP, index = True, nullable=False)
    deadline = Column(TIMESTAMP, index = True, nullable=False)
    deskripsi = Column(Text, index = True, nullable=False)