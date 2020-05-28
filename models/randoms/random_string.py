import uuid

class random_string:
    
    # def __init__(self):
        
    @staticmethod
    def ustring():
        return uuid.uuid4().hex[:8].upper()