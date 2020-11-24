import uuid

from time import perf_counter

from fastapi import FastAPI, Request

from full_api.utils.logger import log_request
from full_api.settings import envs


class Middleware:

    def __init__(self, app: FastAPI):
        app.middleware('http')(self.middleware_main)

    @classmethod
    async def middleware_main(cls, request: Request, callnext):
        local = envs.LOG_LOCAL
        id = str(uuid.uuid1())
        ip, method, path = request.client.host, request.method, cls._get_url_route(request)

        if not envs.LOGGER_SWAGGER and path in envs.LOGGER_IGNORE:
            return await callnext(request)

        log_request("REQUEST RECEBIDA", method, id, ip, path, None, local)
        start_time = perf_counter()
        response = await callnext(request)
        process_time = f'{perf_counter() - start_time:.4f}'
        log_request("REQUEST FINALIZADA", method, id, ip, path, process_time, local)

        response.headers["X-Process-Time"] = process_time
        return response


    @staticmethod
    def _get_url_route(request: Request) -> str:
            try:
                return [route for route in request.scope['router'].routes if route.endpoint == request.scope['endpoint']][0].path
            except KeyError:
                return request.url.path
