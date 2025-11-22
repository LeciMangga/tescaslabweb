from fastapi import APIRouter
from schemas.tp import TPCreate, TPRead, TPUpdate,
from db.session import get_db
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.tp import createTP, readAllTP, updateTP, deleteTP

router = APIRouter(prefix="/tp")

@router.post("/createtp")
async def create_tp(tp: TPCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_tp = await createTP(db, tp)
        return True
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/readalltp")
async def read_all_tp(db: AsyncSession = Depends(get_db)):
    try:
        tps = await readAllTP(db)
        return tps
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.post("/updatetp")
async def update_tp(tp: TPUpdate, db: AsyncSession = Depends(get_db)):
    try:
        hasil = await updateTP(db, tp)
        return hasil
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.post("deletetp")
async def delete_tp(tp: TPUpdate, db: AsyncSession = Depends(get_db)):
    try:
        hasil = await deleteTP(db, tp)
        return hasil
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
