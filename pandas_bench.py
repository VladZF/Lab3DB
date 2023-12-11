import pandas as pd
from config import *


def run():
    df = pd.read_csv(dataset)
    print(df)
    result = df.query()
    print(result)
    
run()
