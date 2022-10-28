from pydantic import BaseModel
from typing import Optional

class FASTASequence(BaseModel):
    type: str
    name: str
    gene: Optional[str]
    locus_tag: str
    db_xref: str
    protein: Optional[str]
    protein_id: Optional[str]
    location: str
    gbkey: str
    transl_except: Optional[str]
    partial: Optional[str]
    sequence: str