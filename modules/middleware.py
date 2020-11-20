import uuid

from time import perf_counter

from fastapi import FastAPI, Request

from full_api.utils.logger import log_request
from full_api.settings import envs


class Middleware:

    def __init__(self, app: FastAPI):
        app.middleware('http')(self.middleware_main)

    @staticmethod
    async def middleware_main(request: Request, callnext):
        id = str(uuid.uuid1())
        ip, method, path = request.client.host, request.method, request.url.path

        if not envs.LOGGER_SWAGGER and path in envs.LOGGER_IGNORE:
            return await callnext(request)

        log_request("REQUEST RECEBIDA", method, id, ip, path)
        start_time = perf_counter()
        response = await callnext(request)
        process_time = f'{perf_counter() - start_time:.4f}'
        log_request("REQUEST FINALIZADA", method, id, ip, path, process_time)

        response.headers["X-Process-Time"] = process_time
        return response
