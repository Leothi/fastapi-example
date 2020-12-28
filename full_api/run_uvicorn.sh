uvicorn api:app --host 0.0.0.0 --port=8080 --reload --no-access-log
# --no-access-log desabilita o logging padrão do uvicorn para requests - Função própria definida no utils