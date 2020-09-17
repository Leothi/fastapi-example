class User():
    def __init__(self, id_: int, name: str, job: str = "", password: str = "swordfish"):
        self.id_ = id_
        self.name = name
        self.job = job
        self.password = password

    def user_attributes(self) -> dict:
        return self.__dict__

