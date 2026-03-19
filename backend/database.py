import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


load_dotenv(Path(__file__).resolve().parent / ".env")


DEFAULT_DB_PATH = Path(__file__).resolve().parent / "hotel.db"
# Convert path to forward slashes for SQLite compatibility on Windows
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{str(DEFAULT_DB_PATH).replace(chr(92), '/')}")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
