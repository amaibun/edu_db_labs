class Dataset():
    def __init__(self, id, title, description, created_at, updated_at, format, license, dataset_status, orginization_id, category_id, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.format = format
        self.license = license
        self.dataset_status = dataset_status
        self.organization_id = orginization_id
        self.category_id = category_id
        self.user_id = user_id
        
    def __repr__(self):
        return f"Dataset:\nid={self.id}\ntitle={self.title}\ndescription={self.description}\ncreated at={self.created_at}\nupdated_at={self.updated_at}\nformat={self.format}\nlicense={self.license}\ndataset status={self.dataset_status}\norganization id={self.organization_id}\ncategory id={self.category_id}\nuser id={self.user_id}"
        