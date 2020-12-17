from typing import List, Optional

from full_api.database.default.sql_alchemy.connector import Connector
from full_api.database.default.sql_alchemy import Declarative_base


class SQLBaseModel:
    
    @classmethod
    def find_one(cls, connection: Connector, identifier: int) -> Declarative_base:
        result = connection.query(cls).get(identifier)
        return result
    
    def insert(self, connection: Connector, *, commit: bool = True):
        connection.session.add(self)
        if commit:
            connection.commit()

    def to_dict(self, *, excluir: Optional[List[str]] = None, parser=True) -> dict:
        if not excluir:
            excluir = []
        if parser:
            return {self.parser[attr]: getattr(self, attr)
                    for attr in self.__dir__() if attr.isupper() and attr not in excluir}
        else:
            return {attr: getattr(self, attr)
                    for attr in self.__dir__() if attr.isupper() and attr not in excluir}
