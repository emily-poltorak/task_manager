import uuid

class Task:
    def __init__(self, name, due_date, priority, state):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.state = state
        self.id = str(uuid.uuid1()) 
        
    def __repr__(self):
        return f"{self.name}, Due: {self.due_date}, Priority: {self.priority}, State: {self.state}"