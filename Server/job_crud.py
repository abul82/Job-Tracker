from sqlalchemy.orm import Session
import job_model
import job_schema

def get_job_application_by_id(db: Session,  sl_id: int):
    return  db.query(job_model.Application).filter(job_model.Application.id == sl_id).first()


def get_job_by_job_id(db: Session, job_id: str):
    """
    This method will return single job details based on job_id
    :param db: database session object
    :param job_id: job id only
    :return: data row if exist else None
    """
    return db.query(job_model.Jobs).filter(job_model.Jobs.job_id == job_id).first()


def get_job_by_id(db: Session, sl_id: int):
    """
    This method will return single job details based on id
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: data row if exist else None
    """
    return db.query(job_model.Jobs).filter(job_model.Jobs.id == sl_id).first()

def get_application(db: Session, skip: int = 0, limit: int = 100):

    return db.query(job_model.Application).offset(0).limit(100).all()


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all job details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(job_model.Jobs).offset(skip).limit(limit).all()

def add_application(db: Session, job: job_schema.JobApply):
    applicant_details = job_model.Application(
        application_id = job.application_id,
        job_id = job.job_id,
        job_name = job.job_name,
        applicant_id =job.applicant_id,
        applicant_name = job.applicant_name,
        applicant_phone = job.applicant_phone,
        applicant_email = job.applicant_email,
        applied_time = job.applied_time
        )
    db.add(applicant_details)
    db.commit()
    db.refresh(applicant_details)
    return job_model.Application(**job.dict())


def add_job_details_to_db(db: Session, job: job_schema.JobAdd):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param db: database session object
    :param job: Object of class job_schema.JobAdd
    :return: a dictionary object of the record which has inserted
    """
    job_details = job_model.Jobs(
        job_id=job.job_id,
        job_name=job.job_name,
        description=job.description,
        role=job.role,
        experience=job.experience,
        qualification=job.qualification,
        job_location=job.job_location,
        salary=job.salary
    )
    db.add(job_details)
    db.commit()
    db.refresh(job_details)
    return job_model.Jobs(**job.dict())


def update_job_details(db: Session, sl_id: int, details: job_schema.UpdateJob):
    """
    this method will update the database
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :param details: Object of class job_schema.Updatejob
    :return: updated job record
    """
    db.query(job_model.Jobs).filter(job_model.Jobs.id == sl_id).update(vars(details))
    db.commit()
    return db.query(job_model.Jobs).filter(job_model.Jobs.id == sl_id).first()

def delete_application(db: Session, sl_id: int):
    try:
        db.query(job_model.Application).filter(job_model.Application.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


def delete_job_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: None
    """
    try:
        db.query(job_model.Jobs).filter(job_model.Jobs.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
