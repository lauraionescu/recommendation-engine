# Content-based recommendation engine

### To run in Python virtual environment
```
  python3 -m venv .
  source bin/activate
  pip3 install -r requirements.txt
```

### To run in Docker
```
docker-compose build
ARTICLE_PATH=<path/to/data> docker-compose run --rm web <text_keyword> <topic_keyword> results.txt
```

### To run the tests
```
  pytest tests
```
