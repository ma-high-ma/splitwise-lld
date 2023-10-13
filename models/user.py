class User:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    def get_phone(self):
        return self.phone

    def set_phone(self, value):
        self.phone = value
