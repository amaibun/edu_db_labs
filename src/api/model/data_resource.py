class DataResource:
    def __init__(self, id, file_name, file_type, size, url, uploaded_at, dataset_id):
        self.id = id
        self.file_name = file_name
        self.file_type = file_type
        self.size = size
        self.url = url
        self.uploaded_at = uploaded_at
        self.dataset_id = dataset_id

    def __repr__(self):
        return f"DataResource(id={self.id}, file_name={self.file_name}, size={self.size})"
