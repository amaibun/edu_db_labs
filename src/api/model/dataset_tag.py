class DatasetTag:
    def __init__(self, dataset_id, tag_id):
        self.dataset_id = dataset_id
        self.tag_id = tag_id

    def __repr__(self):
        return f"DatasetTag(dataset_id={self.dataset_id}, tag_id={self.tag_id})"
