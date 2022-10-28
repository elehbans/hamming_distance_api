import pandas as pd
import numpy as np
from sqlite3 import Connection

from api.config import Config
from api.utils.hamming_distance import hamming_distance

HEADERS = [
    "row_id",
    "type",
    "name",
    "gene",
    "locus_tag",
    "db_xref",
    "protein",
    "protein_id",
    "location",
    "gbkey",
    "transl_except",
    "partial",
    "sequence"
]

def get_sequences(conn: Connection,  target_sequence: str, allowed_distance: int = 1) -> pd.DataFrame:
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {Config.TABLE_NAME}')
    data = cur.fetchall()
    conn.close()
    df = pd.DataFrame(data)
    df.columns = HEADERS
    distances = df['sequence'].apply(lambda x: hamming_distance(x, target_sequence))
    valid_sequences = distances <= allowed_distance
    valid_df = df[np.array(valid_sequences, dtype=bool)]
    return valid_df