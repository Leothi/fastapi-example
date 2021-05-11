from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from api.settings import envs

# Engine para conexão com banco
engine = create_engine(envs.SQL_URI)

# Session do banco
Session = sessionmaker()

# Classe declarativa base do banco
Declarative_base = declarative_base(engine)

from api.database.default.sql_alchemy import *  # noqa

Declarative_base.metadata.create_all(engine)
