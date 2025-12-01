import psycopg
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def load_movies():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM public.movies", conn)
    conn.close()
    return df
