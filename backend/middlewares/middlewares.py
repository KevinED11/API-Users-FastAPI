from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware


middlewares: dict[str, type[GZipMiddleware | CORSMiddleware]] = {
    "gzip": GZipMiddleware,
    "cors": CORSMiddleware
}

gzip_middleware: type[GZipMiddleware] = middlewares["gzip"]
cors_middleware: type[CORSMiddleware] = middlewares["cors"]


