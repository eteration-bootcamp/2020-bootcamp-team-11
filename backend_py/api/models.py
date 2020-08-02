from sqlalchemy import inspect
from dataclasses import dataclass
from api import db

@dataclass
class Job(db.Model):
    __tablename__ = "jobs"
    id = db.Column(db.Integer, primary_key=True)
    jobName = db.Column('name', db.String(255))
    jobCompany = db.Column('company', db.String(255))
    jobDescription = db.Column('description', db.String(255))
    jobLocation = db.Column('location', db.String(255))
    jobContract = db.Column('contract', db.String(255))
    jobTags = db.Column('tags', db.String(255))
    jobNew = db.Column('new', db.Boolean)
    jobFeatured = db.Column('featured', db.Boolean)
    jobDate = db.Column('time', db.TIMESTAMP)
    def __init__(self, jobName, jobCompany, jobDescription, jobLocation, jobContract, jobTags, jobNew, jobFeatured, jobDate):
        self.jobName = jobName
        self.jobCompany = jobCompany
        self.jobDescription = jobDescription
        self.jobLocation = jobLocation
        self.jobContract = jobContract
        self.jobTags = jobTags
        self.jobNew = jobNew
        self.jobFeatured = jobFeatured
        self.jobDate = jobDate
    def as_dict(self):
        return {"id":self.id,"jobName":self.jobName,"jobCompany":self.jobCompany,"jobDescription":self.jobDescription,"jobLocation":self.jobLocation,"jobContract":self.jobContract,"jobTags":self.jobTags,"jobNew":self.jobNew,"jobFeatured":self.jobFeatured,"jobDate":self.jobDate.__str__()}
        #return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
