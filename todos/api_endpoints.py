from starlette.responses import JSONResponse

from .api_datastore import create_todo_item, list_todos


async def api_todo_item_create(request):
    todo_item = await request.json()
    created_todo_item = create_todo_item(todo_item)
    return JSONResponse(status_code=201, content=created_todo_item)


def api_list_todo_items(request):
    todo_items_list = list_todos()
    return JSONResponse(status_code=200, content=todo_items_list)
