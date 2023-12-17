import psycopg2
from config import *
from time import perf_counter
import locale
locale.setlocale(locale.LC_ALL, "ru_RU")



def run():
   result = open(f"{RESULT_FILE_FOLDER}\\results.txt", 'a')
   connect = psycopg2.connect(**DB_PARAMS)
   cursor = connect.cursor()
   print('Psycopg2 test:')
   result.write('Psycopg2 test:\n')
   for query in QUERIES:
      average_time = 0
      for _ in range(ATTEMPT_COUNT):
         start = perf_counter()
         cursor.execute(query)
         finish = perf_counter()
         average_time += finish - start
      average_time /= ATTEMPT_COUNT
      print(f"Query {QUERIES.index(query) + 1}: {locale.str(round(average_time, 3))} seconds")
      result.write(str(locale.str(round(average_time, 3))) + '\n')
   
   cursor.close()
   connect.close()
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