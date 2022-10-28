DROP TABLE IF EXISTS fasta_sequences;

CREATE TABLE fasta_sequences (
    type TEXT, 
    name TEXT,
    gene TEXT, 
    locus_tag TEXT, 
    db_xref TEXT, 
    protein TEXT, 
    protein_id TEXT
    location TEXT, 
    gbkey TEXT, 
    transl_except TEXT,
    partial TEXT,
    sequence TEXT NOT NULL
)