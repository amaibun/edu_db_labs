import uuid

class Tag():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Tag:\nid={self.id}\nname={self.name}"