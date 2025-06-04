class AccessLog():
    def __init__(self, id, accessed_at, user_id, dataset_id):
        self.id = id 
        self.accessed_at = accessed_at
        self.user_id = user_id
        self.dataset_id = dataset_id

    def __repr__(self):
        return f"AccessLog:\nid={self.id}\naccessed at={self.accessed_at}\nuser id={self.user_id}\ndataset id={self.dataset_id}"