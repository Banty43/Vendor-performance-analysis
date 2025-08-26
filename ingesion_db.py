!pip install sqlalchemy
from sqlalchemy import create_engine
import pandas as pd 
import os 
import time
import logging

# Basic logging setup
logging.basicConfig(
    filename="logs/inventory.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
engine = create_engine("mysql+pymysql://root:Banty&2003@localhost:3306/inventory")
def ingest_db(file_path, table_name, engine, chunk_size=300000):
    "Reads CSV in chunks and uploads to MySQL"
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        chunk.to_sql(table_name, con=engine, if_exists='append', index=False)
        print(f"Inserted {len(chunk)} rows into {table_name}")

# Loop through all files in folder



def load_raw_data():
    start = time.time()



for file in os.listdir('data'):
        if file.endswith('.csv'):
            file_path = os.path.join('data', file)
            table_name = file[:-4]  # remove .csv extension
            logging.info(f"Ingesting {file} into db")
            ingest_db(file_path, table_name, engine)
    
    end = time.time()
    total_time = (end - start) / 60
    logging.info('Ingestion complete')
    logging.info(f"Total time taken: {total_time:.2f} minutes")


if __name__ =='__main__':
    load_raw_data()