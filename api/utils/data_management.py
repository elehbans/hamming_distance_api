import os
import pandas as pd
from sqlite3 import Connection
from typing import List

from api.config import Config
from api.db.models import FASTASequence
from api.utils.parse_fasta import parse_fasta

def parse_sample_data() -> List[FASTASequence]:
    api_utils_dir = os.path.dirname( os.path.realpath(__file__))
    sample_data_file = os.path.join(api_utils_dir, 'sample_data.txt')
    f = open(sample_data_file, 'r')
    sample_text = f.read()
    data = parse_fasta(sample_text)
    
    return data

def insert_sample_data(data: list[FASTASequence], conn: Connection) -> None:
    sequences_df = pd.DataFrame([s.__dict__ for s in data])
    sequences_df.to_sql(Config.TABLE_NAME, conn, if_exists="replace")
