from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is not None and job is not None:
            if isinstance(name, str) and isinstance(job, str):
                if self.search_user_by_name(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "User added"
                else:
                    return "User already existent"
            else:
                return "Parameter not valid"
        else:
            return "Parameter not valid"

    def search_user_by_name(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def remove_user(self, name):
        if name is not None:
            if isinstance(name, str):
                if self.search_user_by_name(name) is not None:
                    for user in self.store.bd:
                        if name == user.name:
                            self.store.bd.remove(user)
                        return "User removed"
                else:
                    return "User not existent"
            else:
                return "Parameter not valid"
        else:
            return "Parameter not valid"

    def update_user(self, name, newname):
        if name is not None and newname is not None:
            if isinstance(name, str) and isinstance(newname, str):
                if self.search_user_by_name(name) is not None:
                    for i, user in enumerate(self.store.bd):
                        self.store.bd[i] = newname
                        return "User updated"
                else:
                    return "User not existent"
            else:
                return "Parameter not valid"
        else:
            return "Parameter not valid"

    def get_user_by_name(self, name):
        if name is not None:
            if isinstance(name, str):
                if self.search_user_by_name(name) is not None:
                    for user in self.store.bd:
                        if user.name == name:
                            return name
                else:
                    return "User not found"
            else:
                return "Parameter not valid"
        else:
            return "Parameter not valid"
