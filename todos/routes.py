from starlette.routing import Mount, Route

from .api_endpoints import api_list_todo_items, api_todo_item_create
from .endpoints import (list_todo_list, todo_item_create, todo_list_create,
                        todo_list_delete, todo_list_detail, todo_list_edit)

routes = [
    Mount(
        "/lists",
        name="todo_lists",
        routes=[
            Route(
                "/",
                list_todo_list,
                name="list_todo_list",
                methods=["GET"],
            ),
            Route(
                "/create",
                todo_list_create,
                name="todo_list_create",
                methods=["GET", "POST"],
            ),
            Route(
                "/{todo_list_id}",
                todo_list_detail,
                name="todo_list_detail",
                methods=["GET"],
            ),
            Route(
                "/{todo_list_id}/edit",
                todo_list_edit,
                name="todo_list_edit",
                methods=["GET", "POST"],
            ),
            Route(
                "/{todo_list_id}/delete",
                todo_list_delete,
                name="todo_list_delete",
                methods=["GET", "POST"],
            ),
        ],
    ),
    Mount(
        "/items",
        name="todo_items",
        routes=[
            Route(
                "/create",
                todo_item_create,
                name="todo_item_create",
                methods=["GET", "POST"],
            )
        ],
    ),
    Mount(
        "/api",
        name="apis",
        routes=[
            Route("/create", api_todo_item_create, methods=["POST"]),
            Route("/list", api_list_todo_items, methods=["GET"]),
        ],
    ),
]
