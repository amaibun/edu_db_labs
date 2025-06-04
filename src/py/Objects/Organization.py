class Organization():
    def __init__(self, id, name, description, contact_email, website):
        self.id = id
        self.name = name
        self.description = description
        self.contact_email = contact_email
        self.website = website
    
    def __repr__(self):
        return f"Organization:\nid={self.id}\nname={self.name}\ndescription={self.description}\ncontact email={self.contact_email}\nwebsite={self.website}"