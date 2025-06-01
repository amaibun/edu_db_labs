class Tag:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Tag(id={self.id}, name={self.name})"
