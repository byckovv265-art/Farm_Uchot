from random import randint

from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from src.db.session import Base


class LiveStock(Base):
    __tablename__ = 'livestock'

    vin: Mapped[str] = mapped_column(String, primary_key=True, default =  f'vin{randint(0,10000)}')
    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    sex: Mapped[str] = mapped_column(String, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    state: Mapped[str] = mapped_column(String, nullable=False)

class Feed(Base):
    __tablename__ = 'feed'
    
       
