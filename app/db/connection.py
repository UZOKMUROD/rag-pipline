from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from app.config import sql_dir




vector_engine = create_engine(sql_dir, echo=False, connect_args={'check_same_thread': False})
VectoreSession = sessionmaker(bind=vector_engine, autoflush=False, autocommit=False)
VectorBase = declarative_base()




