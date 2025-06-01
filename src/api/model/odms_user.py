class ODMSUser:
    def __init__(self, id, username, email, role):
        self.id = id
        self.username = username
        self.email = email
        self.role = role  # ENUM: 'Admin', 'Publisher', 'Viewer'

    def __repr__(self):
        return f"ODMSUser(id={self.id}, username={self.username}, role={self.role})"
