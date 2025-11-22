from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update,delete
from db.session import get_db
from schemas.tp import TPCreate, TPRead, TPUpdate
from model.tp import TP
from datetime import datetime

import traceback

async def createTP(db: AsyncSession, tp: TPCreate):
    try:
        db_tp = TP(
            judul = tp.judul,
            subjudul = tp.subjudul,
            kategori = tp.kategori,
            tanggalpost = datetime.now(),
            deadline = datetime.now(),
            deskripsi = tp.deskripsi
        )
        db.add(db_tp)
        await db.commit()
    except Exception as e:
        traceback.print_exc()
        raise

async def readAllTP(db: AsyncSession):
    try:
        hasil = await db.execute(select(TP))
        hasilread = hasil.scalars().all()
        return hasilread
    except Exception as e:
        traceback.print_exc()
        raise

async def updateTP(db: AsyncSession, tp: TPUpdate):
    try:
        check_judul = await db.execute(select(TP).where(TP.id == tp.id))
        check_judul_hasil = check_judul.scalars().first()
        if not check_judul_hasil:
            raise ValueError("TP tidak ditemukan")
        updates = await db.execute(update(TP).where(TP.id == tp.id).values(
            judul = tp.judul,
            subjudul = tp.subjudul,
            kategori = tp.kategori,
            tanggalpost = tp.tanggalpost,
            deadline = tp.deadline,
            deskripsi = tp.deskripsi

        ))
        return updates
    except Exception as e:
        traceback.print_exc()
        raise 
    
async def deleteTP(db: AsyncSession, tp: TPUpdate):
    try:
        check_id = await db.execute(select(TP).where(TP.id == tp.id))
        check_id_hasil = check_id.scalars().first()
        if not check_id_hasil:
            raise ValueError("TP tidak ditemukan")
        updates = await db.execute(delete(TP).where(TP.id == tp.id))
        return updates
    except Exception as e:
        traceback.print_exc()
        raise 