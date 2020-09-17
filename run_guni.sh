gunicorn -b 0.0.0.0:8000 --workers=1 --reload --worker-class=uvicorn.workers.UvicornWorker full_api:app 
# uvicorn full_api:app --reload