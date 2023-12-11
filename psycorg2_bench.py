import psycopg2
from queries import queries
from time import time
from config import *



    
def run():
    
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        for query in queries:
            average_time = 0
            for _ in range(ATTEMPT_COUNT):
                start = time()
                cursor.execute(query)
                finish = time()
                average_time += finish - start
            average_time /= ATTEMPT_COUNT
            print(f"query {queries.index(query)}: {average_time} seconds")
    
        
        cursor.close()
        connection.close()
        
    except psycopg2.Error as e:
        print('Ошибка подключения к БД: ', e)
    
    
