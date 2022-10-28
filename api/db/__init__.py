from flask import Flask
from os.path import dirname, abspath
import os
import sqlite3

from api.config import Config

def init_db(app: Flask) -> sqlite3.Connection:
    print("init db")
    conn = sqlite3.connect(app.config['DATABASE_NAME'])
    schema_file_path = os.path.join(dirname(abspath(__file__)),'schema.sql')
    with open(schema_file_path) as f:
        conn.executescript(f.read())
    
    conn.commit()
    return conn