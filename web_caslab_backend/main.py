from fastapi import FastAPI

from api.v1 import tp
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Tes Caslab", version="0.1.0")

origins =[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    tp.router,
    prefix="/api/v1",
)