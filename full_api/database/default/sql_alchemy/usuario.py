from sqlalchemy import String, Column, Integer, VARCHAR

from full_api.database import Declarative_base
from full_api.database.default.sql_alchemy.base import SQLBaseModel


class UsuarioSQLDatabase(Declarative_base, SQLBaseModel):
    __tablename__ = "USUARIO"

    ID = Column(Integer, primary_key=True)
    NAME = Column(VARCHAR, nullable=False)
    JOB = Column(String(32), nullable=False)
    PW = Column(String(32))
