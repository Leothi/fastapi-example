import uvicorn

from full_api.settings import envs


def start():
    uvicorn.run('full_api:app',
                host=envs.FASTAPI_HOST, port=envs.FASTAPI_PORT,
                reload=envs.FASTAPI_RELOAD, access_log=envs.FASTAPI_ACCESS_LOG)


if __name__ == '__main__':
    start()
