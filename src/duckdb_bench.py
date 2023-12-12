import duckdb
from config import *
from time import perf_counter

QUERIES = [
    """SELECT "VendorID", COUNT(*)
        FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", AVG("total_amount")
       FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*)
       FROM trips GROUP BY 1, 2;""",
    """SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
]

def run():
    connect = duckdb.connect('dbs\\database.db')
    cursor = connect.cursor()
    cursor.execute('INSTALL sqlite')
    print('DuckDB test:')
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