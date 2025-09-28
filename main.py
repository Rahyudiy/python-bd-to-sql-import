import pandas as pd
from sqlalchemy import create_engine

# /change this code to your csv file direction
csvFile = r"C:\Users\gdeng\Downloads\archive (2)\sign_mnist_train.csv"

# change this to your sql account
user = "root"
password = ""
host = "localhost" 
database = "test-bd-2"

print("Scanning CSV Files...")
print("Sabar Bos")

df = pd.read_csv(csvFile, encoding="utf-8")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

print("Importing file to mySql...")

df.to_sql("table-data", engine, if_exists="replace", index=False, chunksize=1000)

print("Done bosku..")
