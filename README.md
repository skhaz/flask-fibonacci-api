

### Develop locally with Python's venv

First, create a virtual environment:

```
python3 -m venv venv
```

Activate the virtual environment:

```
. venv/bin/activate
```

Then install the requirements for development:

```
pip install -r requirements/development.txt
```

To run in debug mode and with auto-reload upon code changes:

```
export FLASK_APP=app/main.py
export FLASK_ENV=development
flask run
```

or using the Makefile

```
make run
```

#### Run lint

```
make lint
```

#### Run black auto-formatter

```
make format
```

#### Clean all cache files

```
make clean
```

### Run tests

```
make test
```

#### Watch for tests

You'll need [entr](http://eradman.com/entrproject/) installed, then run

```
make watch
```

### Run with Docker

First, build it:

```
DOCKER_BUILDKIT=0 docker build --tag fibonacci:latest .
```

Then run

```
docker run -p 5000:5000 -it fibonacci:latest
```

To test if it is working

```
curl "http://localhost:5000/fib?n=10"
```

### Deploy in Google Cloud Run

#### Build

First, create a project on [Google Cloud console](https://console.cloud.google.com/), then export the "project id"

```
export PROJECT_ID=your-project-id
gcloud builds submit --tag gcr.io/$PROJECT_ID/fibonacci
```

#### Deploy

```
gcloud run deploy fibonacci --image gcr.io/$PROJECT_ID/fibonacci --platform managed
```
