class ODMSUser():
    def __init__(self, id, username, email, user_role):
        self.id = id
        self.username = username
        self.email = email
        self.user_role = user_role
        
    def __repr__(self):
        return f"ODMSUser:\nid={self.id}\nusername={self.username}\nemail={self.email}\nuser role={self.user_role}"