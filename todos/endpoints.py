from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from .datastore import (create_todo_item, create_todo_list, delete_todo_list,
                        edit_todo_list, get_todo_list, get_todo_lists,
                        get_todo_lists_items)

templates = Jinja2Templates(directory="todos/templates")


# List view for to-do lists
def list_todo_list(request: Request):
    todo_lists = get_todo_lists()
    context = {
        "request": request,
        "todo_lists": todo_lists,
    }
    return templates.TemplateResponse("list.html", context)


# Create view for a to-do list
async def todo_list_create(request: Request):
    if request.method == "POST":
        form = await request.form()
        todo_list = {
            "name": form.get("name"),
        }
        create_todo_list(todo_list)
        return RedirectResponse(
            url=request.url_for("todo_lists:list_todo_list"), status_code=302
        )
    else:
        context = {"request": request}
        return templates.TemplateResponse("create_list.html", context)


# Detail view for a to-do list
def todo_list_detail(request: Request):
    todo_list_id = request.path_params["todo_list_id"]
    todo_list = get_todo_list(todo_list_id)
    todo_list_items = get_todo_lists_items(todo_list["_id"])
    context = {
        "request": request,
        "todo_list": todo_list,
        "todo_list_items": todo_list_items,
    }
    return templates.TemplateResponse("detail_list.html", context)


# Edit view for a to-do list
async def todo_list_edit(request: Request):
    if request.method == "POST":
        todo_list_id = request.path_params["todo_list_id"]
        form = await request.form()
        todo_list = {
            "name": form.get("name"),
        }
        edit_todo_list(todo_list_id, todo_list)
        return RedirectResponse(
            url=request.url_for(
                "todo_lists:todo_list_detail", todo_list_id=todo_list_id
            ),
            status_code=302,
        )
    else:
        context = {"request": request}
        return templates.TemplateResponse("edit_list.html", context)


# Delete view for a to-do list
async def todo_list_delete(request: Request):
    if request.method == "POST":
        todo_list_id = request.path_params["todo_list_id"]
        delete_todo_list(todo_list_id)
        return RedirectResponse(
            url=request.url_for("todo_lists:list_todo_list"), status_code=302
        )
    else:
        context = {"request": request}
        return templates.TemplateResponse("delete_list.html", context)


# Create view for a to-do item
async def todo_item_create(request: Request):
    if request.method == "POST":
        form = await request.form()
        todo_item = {
            "task": form.get("task"),
            "due_date": form.get("due_date"),
            "is_completed": form.get("is_completed"),
            "list": form.get("list"),
        }
        create_todo_item(todo_item)
        return RedirectResponse(
            url=request.url_for("todo_lists:list_todo_list"), status_code=302
        )
    else:
        todo_lists = get_todo_lists()
        context = {"request": request, "todo_lists": todo_lists}
        return templates.TemplateResponse("create_item.html", context)
