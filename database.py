import os
from sqlalchemy import create_engine, text

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
      