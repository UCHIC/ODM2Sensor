class User:
    def is_authenticated(self):
        return True

class Request:
    def __init__(self, method, path):
        self.user = User()
        self.method = method
        self.path = path