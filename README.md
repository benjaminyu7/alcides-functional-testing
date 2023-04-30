Functional testing for alcides by testing the app APIs

# Build
docker build -t pytest-restapi .

# Run
docker run --rm -v ${PWD}:/app pytest-restapi