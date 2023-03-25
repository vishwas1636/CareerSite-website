import os
from sqlalchemy import create_engine, text
from flask import request


db_con_string = os.environ['DB_CON_STRING']

engine = create_engine(db_con_string,
                       connect_args={'ssl': {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as con:
    result = con.execute(text('select * from jobs'))

    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_all = result.all()
        first_result = result_all[int(id)-1]
        column_names = result.keys() 
        first_result_dict = dict(zip(column_names, first_result))
        return (first_result_dict)

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
          query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
  
          conn.execute(query, {
              'job_id': job_id,
              'full_name': data['full_name'],
              'email': data['email'],
              'linkedin_url': data['linkedin_url'],
              'education': data['education'],
              'work_experience': data['work_experience'],
              'resume_url': data['resume_url']
          })
  
    
  
  