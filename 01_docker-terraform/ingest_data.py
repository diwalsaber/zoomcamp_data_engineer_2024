import argparse
import os
import time
import pandas as pd
from sqlalchemy import create_engine

parser = argparse.ArgumentParser(description='Ingest data from a CSV file to Postgres.')

# user
# password
# host
# port
# database name
# table name
# url of the csv

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")  

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name, compression='gzip', iterator=True, chunksize=100000)

    try:
        df = next(df_iter)  # Charger le premier chunk pour créer la table
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

        df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')  # Créer la table avec le bon schéma

        while True:
            t_start = time.time()

            df.to_sql(name=table_name, con=engine, if_exists='append')  # Insérer le premier chunk

            df = next(df_iter)  # Charger le chunk suivant
            df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
            df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

            t_end = time.time()
            print(f'inserted another chunk..., took {t_end - t_start} seconds')

    except StopIteration:
        print("Toutes les données ont été traitées.")
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ingest data from a CSV file to Postgres.')    

    parser.add_argument("--user", help="user name for postgres")
    parser.add_argument("--password", help="password for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="database name for postgres")  # Change from '--db' to '--database'
    parser.add_argument("--table_name", help="table name for postgres")  # Change from '--table_name' to '--table'
    parser.add_argument("--url", help="url of the csv")

    args = parser.parse_args()

    main(args)  # Appeler main avec les arguments analysés


