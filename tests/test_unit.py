from typing import Dict, List

from api.db.models import FASTASequence
from api.utils.parse_fasta import parse_fasta
from api.utils.hamming_distance import hamming_distance


def test_parse_fasta(data: Dict):
    results = parse_fasta(data['raw'])

    assert isinstance(results, List)
    assert isinstance(results[0], FASTASequence)
    assert len(results) == 2

def test_hamming_distance_match(data: Dict):
    results = hamming_distance(data['target'], data['match'])
    assert results == 1


def test_hamming_distance_too_short(data: Dict):
    results = hamming_distance(data['target'], data['no-match-too-short'])
    assert results is None


def test_hamming_distance_too_distant(data: Dict):
    results = hamming_distance(data['target'], data['no-match-too-distant'])
    assert results == 3


