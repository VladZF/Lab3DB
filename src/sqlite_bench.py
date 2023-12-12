import pandas as pd
import sqlite3
from config import *
from time import perf_counter

QUERIES = [
    """SELECT "VendorID", COUNT(*)
        FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", AVG("total_amount")
       FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), COUNT(*)
       FROM trips GROUP BY 1, 2;""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
]

def run():
    connect = sqlite3.connect('dbs\\database.db')
    df = pd.read_csv(DATASET)
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
    df.to_sql('trips', connect, if_exists='replace', chunksize=1000, index=False)
    cursor = connect.cursor()


    print('SQLite3 test:')
    for query in QUERIES:
        average_time = 0
        for _ in range(ATTEMPT_COUNT):
            start = perf_counter()
            cursor.execute(query)
            finish = perf_counter()
            average_time += finish - start
        average_time /= ATTEMPT_COUNT
        print(f"Query {QUERIES.index(query) + 1}: {round(average_time, 3)} seconds")

    cursor.close()
    connect.close()