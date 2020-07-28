from dataclasses import dataclass
from api import db

@dataclass
class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    company = db.Column(db.String(200))
    description = db.Column(db.String(200))
    location = db.Column(db.String(200))
    contract = db.Column(db.String(200))
    tags = db.Column(db.String(200))
    new = db.Column(db.Boolean)
    featured = db.Column(db.Boolean)
    time = db.Column(db.TIMESTAMP)
    deleted = db.Column(db.Boolean)
    def __init__(self, name, company, description, location, contract, tags, new, featured, time, deleted):
        self.name = name
        self.company = company
        self.description = description
        self.location = location
        self.contract = contract
        self.tags = tags
        self.new = new
        self.featured = featured
        self.time = time
        self.deleted = deleted
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}