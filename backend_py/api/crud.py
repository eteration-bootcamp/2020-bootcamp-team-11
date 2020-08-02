from api import db
from models import Job
import logging

def get_job(jobid):
    """
    This method returns Job class by job id.

    :param jobid: Requires integer as parameter.
    :return dict: Returns dict of job
    """
    try:
        result = Job.query.filter(Job.id == jobid).first()  # Query by job id
        if result is None:                                  # Return bad status if not found 
            return {"status": 404, "source": "DB"} 
        else:
            resultmod = result.as_dict()                    # Parse as dict for JSON response
            #resultmod["jobDate"] = resultmod["jobDate"].__str__() # Convert datetime object to string for JSON serial.
        return resultmod
    except Exception as exp:
        logging.exception("Exception:" + str(exp))
        return {"status": 404}

def put_job(jobid, receivedjson):
    """
    This method updates Job by job id and returns OK message.

    :param jobid: Requires integer as parameter.
    :return dict: Returns dict of status
    """
    try:
        result = Job.query.filter(Job.id == jobid).first()  # Query by job id
        for key, value in receivedjson.items():             # Iterate over JSON body sent via request
            setattr(result, key, value)                     # Change att. of current job object
        db.session.commit()                                 # Commit to database for persistance
        return result.as_dict()
    except Exception as exp:
        logging.exception("Exception:" + str(exp))
        return {"status": 404}
    
def delete_job(jobid):
    """
    This method deletes Job by job id and returns OK message.

    :param jobid: Requires integer as parameter.
    :return dict: Returns dict of status
    """
    try:
        Job.query.filter_by(id=jobid).delete()              # Delete by job id
        db.session.commit()                                 # Commit to database for persistance
        return {"status": 200}
    except Exception as exp:
        logging.exception("Exception:" + str(exp))
        return {"status": 404}

def get_jobs():
    """
    This method returns all Jobs.

    :return dict: Returns dict of status
    """
    all_jobs = []
    try:
        for jobs in db.session.query(Job.id).order_by(Job.id.asc()):    # Query all job ids
            all_jobs.append(get_job(jobs[0]))                        # Assign id as key and details as value of temp variabile
        return all_jobs
    except Exception as exp:
        logging.exception("Exception:" + str(exp))
        return {"status": 404}
