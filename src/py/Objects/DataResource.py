class DataResource():
    def __init__(self, id, file_name, file_type, size, url, uploaded_at, dataset_id):
        self.id = id
        self.file_name = file_name
        self.file_type = file_type
        self.size = size
        self.url = url
        self.uploaded_at = uploaded_at
        self.dataset_id = dataset_id
    
    def __repr__(self):
        return f"DataResourse:\nid={self.id}\nfile name={self.file_name}\nfile type={self.file_type}\nsize={self.size}\nurl={self.url}\nuploaded at={self.uploaded_at}\ndataset_id{self.dataset_id}"