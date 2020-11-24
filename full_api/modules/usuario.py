from full_api.database.usuario import UsuarioDatabase


def search(insertion_id: str):
    with UsuarioDatabase() as db:
        result = db.search(insertion_id)
    return result

def insert(name: str, job: str, password: str):
    with UsuarioDatabase() as db:
        insertion_id = db.insert(name, job, password)

    return insertion_id
