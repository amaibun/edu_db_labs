import uuid

class Organization:
    def __init__(self, id, name, description, contact_email, website):
        self.id = id
        self.name = name
        self.description = description
        self.contact_email = contact_email
        self.website = website

    def __repr__(self):
        return f"Organization(id={self.id}, name={self.name}, email={self.contact_email})"
