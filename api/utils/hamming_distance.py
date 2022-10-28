from typing import Union

def hamming_distance(sequence_one: str, sequence_two: str) -> Union[int, None]:
    same_length = len(sequence_one) == len(sequence_two)
    if not same_length:
        return None
    else:
        return sum(c1 != c2 for c1, c2 in zip(sequence_one, sequence_two))