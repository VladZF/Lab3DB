from src import *
from config import *
import os


launch = {
    'duckdb': duckdb,
    'pandas': pandas,
    'psycopg2': psycopg2,
    'sqlite': sqlite,
    'sqlalchemy': sqlalchemy
}

f = open(f'{RESULT_FILE_FOLDER}\\results.txt', 'w')
f.close()

for lib in LIB.keys():
    if LIB[lib] == True:
        launch[lib]()






