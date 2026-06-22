from fastapi import FastAPI, Request
from routers import users, posts, cancer
import time
import datetime
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager



@asynccontextmanager
async def event_life_span(app):
    with open("server_time_log.log", "a") as log:
        log.write(f"Application start up at: {datetime.datetime.now()}\n")
    yield()
    with open("server_time_log.log", "a") as log:
        log.write(f"Application shut down at: {datetime.datetime.now()}\n")



app = FastAPI(lifespan=event_life_span)
app.include_router(users.router, tags=['Users'])
app.include_router(posts.router, tags=['Posts'])
app.include_router(cancer.router, tags=['Cancer'])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response


class RateLimitMiddleware(BaseHTTPMiddleware):
    RATE_LIMIT_DURATION = datetime.timedelta(minutes=1)
    RATE_LIMIT_REQUESTS = 10

    def __init__(self, app):
        super().__init__(app)
        self.requests_count = {} # ip: (request_count, last_request)

    async def dispatch(self, request, call_next):
        client_ip = request.client.host
        request_count, last_request = self.requests_count.get(client_ip, (0, datetime.datetime.min))
        elapsed_time = datetime.datetime.now() - last_request
        if elapsed_time > self.RATE_LIMIT_DURATION:
            request_count = 1
        else:
            if request_count >= self.RATE_LIMIT_REQUESTS:
                return JSONResponse(status_code=429, content={'Message': 'Rate limit exceeded! Please try again later.'})
            request_count += 1

        self.requests_count[client_ip] = (request_count, datetime.datetime.now())
        response = await call_next(request)
        return response

app.add_middleware(RateLimitMiddleware)