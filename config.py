# Database parameters
DB_PARAMS = {
    'dbname': '',
    'user': '',
    'password': '',
    'host': '',
    'port': 0
}

# Number of launch for each query (recommended value is 20)
ATTEMPT_COUNT = 1

# path to dataset file (.db for example)
DATASET = 'E:\\Projects\\lab3_db\\data\\database.db'

# queries for execution
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

# path to txt file with average query execution times
RESULT_FILE_FOLDER = 'data'

# Library for testing (True - lib launchs for test, False - lib doesn't launch)
LIB = {
    'pandas': False,
    'sqlite': False,
    'psycopg2': False,
    'duckdb': True,
    'sqlalchemy': False
}




