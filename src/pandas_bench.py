import pandas as pd
import sqlalchemy
from time import perf_counter 
from config import *


def run():
    URL_TO_DB = f'postgresql://{DB_PARAMS["user"]}:{DB_PARAMS["password"]}@{DB_PARAMS["host"]}:{DB_PARAMS["port"]}/{DB_PARAMS["dbname"]}'
    engine = sqlalchemy.create_engine(URL_TO_DB)
    print('Pandas test:')
    
    for query in QUERIES:
        average_time = 0
        for _ in range(ATTEMPT_COUNT):
            start = perf_counter()
            pd.read_sql(query, con=engine)
            finish = perf_counter()
            average_time += finish - start
        average_time /= ATTEMPT_COUNT
        print(f"Query {QUERIES.index(query) + 1}: {round(average_time, 3)} seconds")
    
    engine.dispose()