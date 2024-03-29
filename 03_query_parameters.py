"""
Query-параметры представляют из себя набор пар ключ-значение, которые идут после знака ? в URL-адресе, разделенные символами &
"""

from __future__ import annotations
from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# Необязательные параметры
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# Преобразование типа параметра запроса
@app.get("/bool_items/{bool_item_id}")
async def read_item(bool_item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"bool_item_id": bool_item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Смешивание query-параметров и path-параметров
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Обязательные query-параметры
@app.get("/required_items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/required_items_2/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    """
    Конечно, вы можете определить некоторые параметры как обязательные,
    некоторые - со значением по умполчанию,
    а некоторые - полностью необязательные:
    :param item_id:
    :param needy:
    :param skip:
    :param limit:
    :return:
    """
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
