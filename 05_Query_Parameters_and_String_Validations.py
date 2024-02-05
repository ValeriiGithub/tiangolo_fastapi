from typing import Union, List
# from pydantic import Required # has been removed in V2.
from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Множество значений для query-параметра
@app.get("/items_2/")
async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
    query_items = {"q": q}
    return query_items

# Query-параметр со множеством значений по умолчанию
@app.get("/items_3/")
async def read_items(q: Annotated[List[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

# Больше метаданных¶
#
# Вы можете добавить больше информации об query-параметре.
# Вы можете указать название query-параметра, используя параметр title:
@app.get("/items_4/")
async def read_items(
    q: Annotated[Union[str, None], Query(title="Query string", min_length=3)] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items_5/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Псевдонимы параметров
@app.get("/items_6/")
async def read_items(q: Annotated[Union[str, None], Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Устаревшие параметры
# Тогда для Query укажите параметр deprecated=True:
@app.get("/items_deprecated/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Исключить из OpenAPI¶
#
# Чтобы исключить query-параметр из генерируемой OpenAPI схемы (а также из системы автоматической генерации документации),
# укажите в Query параметр include_in_schema=False:
@app.get("/Exclude_from_OpenAPI/")
async def read_items(
    hidden_query: Annotated[Union[str, None], Query(include_in_schema=False)] = None
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


"""
Резюме¶

Вы можете объявлять дополнительные правила валидации и метаданные для ваших параметров запроса.

Общие метаданные:

    alias
    title
    description
    deprecated
    include_in_schema

Специфичные правила валидации для строк:

    min_length
    max_length
    regex

В рассмотренных примерах показано объявление правил валидации для строковых значений str.

В следующих главах вы увидете, как объявлять правила валидации для других типов (например, чисел).
"""