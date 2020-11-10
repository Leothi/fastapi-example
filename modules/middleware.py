import uuid

from time import perf_counter

from fastapi import FastAPI, Request

from full_api.utils.logger import log_request


class Middleware:

    def __init__(self, app: FastAPI):
        app.middleware('http')(self.middleware_main)

    @staticmethod
    async def middleware_main(request: Request, callnext):
        id = str(uuid.uuid1())

        log_request("REQUEST RECEBIDA", request.method, id,
                    request.client.host, request.url.path)
        start_time = perf_counter()
        response = await callnext(request)
        process_time = f'{perf_counter() - start_time:.4f}'
        log_request("REQUEST FINALIZADA", request.method, id,
                    request.client.host, request.url.path, process_time)

        response.headers["X-Process-Time"] = process_time
        return response
