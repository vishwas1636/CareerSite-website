import os
from sqlalchemy import create_engine ,text


db_con_string = os.environ['DB_CON_STRING']

engine = create_engine(db_con_string,
                      connect_args={
                        'ssl':{
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })




def load_jobs_from_db():
    with engine.connect() as con:
        result = con.execute(text('select * from jobs'))
      
        jobs=[]
        for row in result.all():
         jobs.append(row._mapping)
        return jobs