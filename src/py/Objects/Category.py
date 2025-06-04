class Category():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return f"Category:\nnid={self.id}\nname={self.name}"