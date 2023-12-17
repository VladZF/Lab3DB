import pandas as pd
import sqlalchemy
from time import perf_counter 
from config import *
import locale
locale.setlocale(locale.LC_ALL, "ru_RU")





def run():
    result = open(f"{RESULT_FILE_FOLDER}\\results.txt", 'a')
    
    url_to_db = f'postgresql://{DB_PARAMS["user"]}:{DB_PARAMS["password"]}@{DB_PARAMS["host"]}:{DB_PARAMS["port"]}/{DB_PARAMS["dbname"]}'
    engine = sqlalchemy.create_engine(url_to_db)
    print('Pandas test:')
    
    result.write('Pandas test:\n')
    for query in QUERIES:
        average_time = 0
        for _ in range(ATTEMPT_COUNT):
            start = perf_counter()
            pd.read_sql(query, con=engine)
            finish = perf_counter()
            average_time += finish - start
        average_time /= ATTEMPT_COUNT
        print(f"Query {QUERIES.index(query) + 1}: {locale.str(round(average_time, 3))} seconds")
        result.write(str(locale.str(round(average_time, 3))) + '\n')
    
    engine.dispose()
    result.close()
    
    
# queries for '4queries' benchmark 

# QUERIES = [
#     """SELECT "VendorID", COUNT(*)
#         FROM trips GROUP BY 1;""",
#     """SELECT "passenger_count", AVG("total_amount")
#        FROM trips GROUP BY 1;""",
#     """SELECT "passenger_count", DATE_PART('Year', tpep_pickup_datetime::date), COUNT(*)
#        FROM trips GROUP BY 1, 2;""",
#     """SELECT "passenger_count", DATE_PART('Year', tpep_pickup_datetime::date), ROUND("trip_distance"), COUNT(*)
#        FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
# ]