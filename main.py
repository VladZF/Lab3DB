from src import *
from config import *


launch = {
    'duckdb': duckdb,
    'pandas': pandas,
    'psycopg2': psycopg2,
    'sqlite': sqlite,
    'sqlalchemy': sqlalchemy
}



for lib in LIB.keys():
    if LIB[lib] == True:
        launch[lib]()






