from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount

from todos import routes as todos_routes


def homepage(request):
    return PlainTextResponse("Hello, world!")


def startup():
    print("Ready to go")


routes = [
    Route("/", homepage),
    Mount("/todos", routes=todos_routes.routes),
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])
