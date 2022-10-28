# Hamming Distance App

## Development

When developing locally the app can be run directly:

```bash
python -m venv venv
source venv/bin/activate
pip install -r api/requirements.txt
cd api
source .env
flask run
```

## Deployment

After cloning the repo and installing Docker Compose, you can deploy the flask API in a container:

```bash
docker-compose build
docker-compose up
```

By default the app uses port `5000`, so requests can be sent to `http://localhost:5000/hamming_distance?sequence=<example_sequence>`

## Testing

Unit tests for the flask API are done with pytest and do not test functionality related to redis. These tests can be run with `python -m pytest tests/test_unit.py` from the root directory.

Integration tests can be run by `python -m pytest tests/test_integration.py`.

## CI / CD

TODO: Github action for each commit runs unit and integration tests

## Hygiene

TODO: Use black for formatting

## Design Discussion
- For demo purposes, I am using flask as it is simple to get up and running.
- For production, this solution seems like it could be a candidate for being implemented in the cloud in a cloud-native way using an API Gateway and then WebAssembly wrapping Rust in Lambda functions, maybe even Lambda@Edge if the package can be made small enough (50Mb limit I think) and then a NoSQL AWS Dynamo DB for data storage (Or redis if we really want to clear it on each upload).  I haven't implemented anything with WebAssembly yet, but the Rust Bioinformatics community seems to be growing.  Essentially, it seems like an intriguing opportunity to push functionality that previously lived in a backend closer to the end user and take advantage of the closest serverless services.
- I am doing a simple hamming distance that looks only for replacement, does not allow insertion/deletion and does not look for partial matches within a larger sequence.  There is also no error handling for unexpected characters outside of `[A,C,T,G]`.  This is done simply for demonstration.
- I have not put together a full test-suite, just those pieces necessary for the success path

