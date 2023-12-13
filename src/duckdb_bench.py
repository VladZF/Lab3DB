import duckdb
from config import *
from time import perf_counter



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