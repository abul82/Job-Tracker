from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import job_crud
import job_model
import job_schema
from db_handler import SessionLocal, engine

job_model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Job Tracker",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1:8000/",
    "http://localhost:5000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/jobs/apply',response_model=job_schema.JobApply)
async def aplly_job(jobApplication: job_schema.JobApply, db: Session = Depends(get_db)):
    # application = job_crud.get_job_application_by_id(db=db, application_id=jobApplication.application_id)
    # if application:
    #     raise HTTPException(status_code=400, detail=f"Application id {jobApplication.application_id} already exist in database: {application_id}")
    return job_crud.add_application(db=db, job=jobApplication)


@app.get('/jobs/applications', response_model=List[job_schema.Application])
async def get_job_applications(skip: int = 0, limit: int = 100,db: Session = Depends(get_db)):
    applications = job_crud.get_application(db=db, skip=skip, limit=limit)
    return applications


@app.get('/jobs', response_model=List[job_schema.Job])
async def retrieve_all_job_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = job_crud.get_jobs(db=db, skip=skip, limit=limit)
    return jobs

@app.post('/jobs', response_model=job_schema.JobAdd)
async def add_new_job(job: job_schema.JobAdd, db: Session = Depends(get_db)):
    job_id = job_crud.get_job_by_job_id(db=db, job_id=job.job_id)
    if job_id:
        raise HTTPException(status_code=400, detail=f"job id {job.job_id} already exist in database: {job_id}")
    return job_crud.add_job_details_to_db(db=db, job=job)



@app.delete('/jobs/application')
async def delete_job_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = job_crud.get_job_application_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        job_crud.delete_application(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.delete('/jobs')
async def delete_job_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = job_crud.get_job_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        job_crud.delete_job_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/jobs', response_model=job_schema.Job)
async def update_job_details(sl_id: int, update_param: job_schema.UpdateJob, db: Session = Depends(get_db)):
    details = job_crud.get_job_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return job_crud.update_job_details(db=db, details=update_param, sl_id=sl_id)




# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
