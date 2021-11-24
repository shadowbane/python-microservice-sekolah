from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from ..database import Base


class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=False, index=True, autoincrement=True)
    uuid = Column(UUID, primary_key=True, index=True, unique=True)
    kode_provinsi = Column(String)
    kode_kab_kota = Column(String)
    kode_kecamatan = Column(String)
    npsn = Column(String, nullable=True)
    name = Column(String)
    bentuk = Column(String)
    status = Column(String)
    alamat_jalan = Column(Text, nullable=True)
    lintang = Column(Float, nullable=True)
    bujur = Column(Float, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)

