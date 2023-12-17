# Database parameters
DB_PARAMS = {
    'dbname': '',
    'user': '',
    'password': '',
    'host': '',
    'port': 0
}

# Number of launch for each query (recommended value is 20)
ATTEMPT_COUNT = 20

# path to dataset file (.db for example)
DATASET = ''

# queries for execution
QUERIES = []

# path to folder where will be txt file with average query execution times
RESULT_FILE_FOLDER = ''

# Library for testing (True - lib launchs for test, False - lib doesn't launch)
LIB = {
    'pandas': False,
    'sqlite': False,
    'psycopg2': False,
    'duckdb': False,
    'sqlalchemy': False
}




