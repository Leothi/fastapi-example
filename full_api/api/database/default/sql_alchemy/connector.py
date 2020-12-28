from api.database import Session


class Connector:
    _session = _query = None

    @property
    def session(self):
        return self._session

    @property
    def query(self):
        return self._query

    def commit(self):
        self.session.commit()

    def flush(self):
        self.session.flush()

    def rollback(self):
        self.session.rollback()

    def refresh(self, instance):
        self.session.refresh(instance)

    # Conexão com context manager
    def __enter__(self):
        self._session = Session()
        self._query = self._session.query
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, Exception):
            self.rollback()
        self.session.close()
