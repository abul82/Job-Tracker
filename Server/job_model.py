from sqlalchemy import Boolean, Column, Integer, String
from db_handler import Base
class Jobs(Base):
    """
    This is a model class. which is having the job table structure with all the constraint
    """
    __tablename__ = "job"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    job_id = Column(String, unique=True, index=True, nullable=False)
    job_name = Column(String(255), index=True, nullable=False)
    description = Column(String(100), index=True, nullable=False)
    role = Column(String, index=True, nullable=False)
    experience = Column(String(100), nullable=False, default=True)
    qualification = Column(String(255), index=True, nullable=False)
    job_location = Column(String, index=True)
    salary = Column(String, index=True)

class Application(Base):
    __tablename__ = "jobapply"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    application_id = Column(String(255), unique=True, index=True, nullable=False)
    job_id = Column(String(255), index=True, nullable=False)
    job_name = Column(String(255), index=True, nullable=False)
    applicant_id = Column(String(255), index=True, nullable=False)
    applicant_name = Column(String(255), index=True, nullable=False)
    applicant_phone = Column(String(255), index=True, nullable=False)
    applicant_email = Column(String(255), index=True, nullable=False)
    applied_time = Column(String(255), index=True, nullable=False)