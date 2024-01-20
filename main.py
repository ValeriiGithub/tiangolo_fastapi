from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    my_model = "my_model"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Выбери название модели
    :param model_name: название модели
    :return: словарь
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
