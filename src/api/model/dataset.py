class Dataset:
    def __init__(self, id, title, description, created_at, updated_at, format,
                 license, status, organization_id, category_id, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.format = format
        self.license = license
        self.status = status
        self.organization_id = organization_id
        self.category_id = category_id
        self.user_id = user_id

    def __repr__(self):
        return f"Dataset(id={self.id}, title={self.title}, status={self.status})"
