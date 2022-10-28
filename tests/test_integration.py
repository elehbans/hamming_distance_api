import json
from flask.testing import FlaskClient
from typing import Dict

# TODO: 
# Failure Modes
# Bad url
# bad request type

# Success Modes
def test_hamming_distance_with_match(client: FlaskClient, data: Dict):
    rv = client.get(f"/hamming_distance?sequence={data['api-input-match']}")
    assert rv is not None

# TODO:
# test_hamming_distance_no_matches


