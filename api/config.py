import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DATABASE_NAME = 'sequences'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, DATABASE_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TABLE_NAME = 'fasta_sequences'
