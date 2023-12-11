db_params = {
    'dbname': 'test',
    'user': 'test',
    'password': 'test',
    'host': 'localhost',
    'port': '5432'
}

queries = [
    """SELECT "VendorID", COUNT(*)
        FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", AVG("total_amount")
       FROM trips GROUP BY 1;""",
    """SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*)
       FROM trips GROUP BY 1, 2;""",
    """SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
]

ATTEMPT_COUNT = 1000

dataset = 'nyc_yellow_tiny.csv'