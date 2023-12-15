from src import duckdb_bench
from src import pandas_bench
from src import psycopg2_bench
from src import sqlite_bench
from src import sqlalchemy_bench
from config import *



launch = {
    'duckdb': duckdb_bench.run,
    'pandas': pandas_bench.run,
    'psycopg2': psycopg2_bench.run,
    'sqlite': sqlite_bench.run,
    'sqlalchemy': sqlalchemy_bench.run
}

for lib in LIB.keys():
    if LIB[lib] == True:
        launch[lib]()






