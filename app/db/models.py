from sqlalchemy import Column, Integer, String
from .connection import VectorBase


class Chunks(VectorBase):

    __tablename__ = "chunks"
    id = Column(Integer, primary_key=True)
    text = Column(String)


