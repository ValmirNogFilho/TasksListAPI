from src import db
import datetime

class Task(db.Model):

    id: int = db.Column(db.Integer(), primary_key=True)
    title: str = db.Column(db.String(length=80), nullable=False)
    description: str = db.Column(db.String(length=500), nullable=False)
    status: int = db.Column(db.Integer(), nullable=False)
    date: date = db.Column(db.Date, nullable=False) 

    def __init__(self, title: str, description: str, status: str, date: datetime.date):
        self.title = title
        self.description = description
        self.status = status
        self.date = date

    def as_dict(self):
        brazilian_formatted_date = datetime.datetime.strftime(self.date, "%d/%m/%Y")
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "date" : brazilian_formatted_date
        }
    
    def update(self, updated_task_request: dict):
        self.title = updated_task_request["title"]
        self.description = updated_task_request["description"]
        self.status = updated_task_request["status"]
        