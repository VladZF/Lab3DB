import pandas as pd
import sqlalchemy
from config import *

server = DB_PARAMS["server"]
user = DB_PARAMS["user"]
password = DB_PARAMS["password"]
host = DB_PARAMS["host"]
port = DB_PARAMS["port"]
dbname = DB_PARAMS["dbname"]

def run():
    engine = sqlalchemy.create_engine(URL_TO_DB)
    df = pd.read_csv(DATASET)
    try:
        df.to_sql(name='trips', con=engine, if_exists="replace",index=False)
    except Exception as e:
        print(e)
        return
    query = 'select * from trips limit 10'
    result = df.read_sql(query, con=engine)
    print(result)