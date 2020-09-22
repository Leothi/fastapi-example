# gunicorn -b 0.0.0.0:8000 --workers=1 --worker-class=uvicorn.workers.UvicornWorker full_api:app --reload
uvicorn full_api:app --reload --no-access-log
# --no-access-log desabilita o logging padrão do uvicorn para requests - Função própria definida no utils