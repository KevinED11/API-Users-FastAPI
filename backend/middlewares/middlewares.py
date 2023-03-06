from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.exceptions import ExceptionMiddleware

middlewares: dict[str, type[GZipMiddleware | CORSMiddleware | ExceptionMiddleware]] = {
    "gzip": GZipMiddleware,
    "cors": CORSMiddleware,
    "exception": ExceptionMiddleware
}

gzip_middleware, cors_middleware, exception_middleware = middlewares["gzip"], middlewares["cors"], middlewares["exception"]
