from typing import Optional
from pydantic import BaseModel



class JobBase(BaseModel):
    job_name:  Optional[str] = None
    description:  Optional[str] = None
    role:  Optional[str] = None



class JobAdd(JobBase):
    job_id: str
    
    experience: Optional[str] = None
    qualification: Optional[str] = None
    job_location: Optional[str] = None
    salary: Optional[str] = None
    
    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    job_id:str
    application_id:str


class JobApply(ApplicationBase):
    
    job_name:Optional[str] = None
    
    applicant_id:Optional[str] = None
    applicant_name:Optional[str] = None
    applicant_phone:Optional[str] = None
    applicant_email:Optional[str] = None
    applied_time:Optional[str] = None

    class Config:
        orm_mode = True



class Application(JobApply):
    id:int
    class Config:
        orm_mode = True


class Job(JobAdd):
    id: int

    
    class Config:
        orm_mode = True


class UpdateJob(BaseModel):
    
    experience: Optional[str] = None
    qualification: Optional[str] = None
    job_location: Optional[str] = None
    salary: Optional[str] = None

    
    class Config:
        orm_mode = True
