import re
from typing import List

from api.db.models import FASTASequence

valid_keys_regex = r'^(gene|locus_tag|db_xref|protein|protein_id|location|gbkey|transl_except|partial)='

def parse_fasta(text: str) -> List[FASTASequence]:
    results = []
    errors = []

    chunks = text.split('>')
    for chunk in chunks[1:]:
        main_split = chunk.split('\n', 1)
        header = main_split[0]
        sequence = re.sub(r"[\n\t\s]*", "", main_split[1])

        header_split = header.split(' ', 1)
        type_name = header_split[0]
        type_name_split = type_name.split('|')
        type = type_name_split[0]
        name = type_name_split[1]

        expected_values = {
            'gene': None,
            'locus_tag': None,
            'db_xref': None,
            'protein': None,
            'protein_id': None,
            'location': None,
            'gbkey': None,
            'transl_except': None,
            'partial': None
        }

        other_fields = header_split[1].split('] [')
        for field in other_fields[1:]:
            field = field.strip('][')
            if re.match(valid_keys_regex, field) is not None:
                splits=field.split('=')
                expected_values[splits[0]]=splits[1]
            else:
                raise Exception('Invalid key found')

        try:
            validated_sequence = FASTASequence(
                type=type,
                name=name,
                gene=expected_values['gene'],
                locus_tag=expected_values['locus_tag'],
                db_xref=expected_values['db_xref'],
                protein=expected_values['protein'],
                protein_id=expected_values['protein_id'],
                location=expected_values['location'],
                gbkey=expected_values['gbkey'],
                transl_except=expected_values['transl_except'],
                partial=expected_values['partial'],
                sequence=sequence
            )
            results.append(validated_sequence)
        except:
            errors.append(chunk)
    
    return results
