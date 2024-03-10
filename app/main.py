from fastapi import FastAPI, Query
from fastapi.openapi.utils import get_openapi

from routers.transaction import router as transaction_router


app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Bitcoin from Blockchair API",
        version="1.0.0",
        description=(
            "Service for collecting data on bitcoin transactions "
            "into a graph database"),
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(transaction_router)
