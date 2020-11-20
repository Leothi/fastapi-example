# gunicorn -b 0.0.0.0:8000 --workers=1 --reload --worker-class=uvicorn.workers.UvicornWorker full_api:app 
# uvicorn full_api:app --reload 
gunicorn -k=uvicorn.workers.UvicornWorker -c=python:full_api.settings full_api:app