from typing import Dict
from pydantic import BaseModel, Field


class ItemSchema(BaseModel):
    item_id: int = Field(...)
    item_name: str = Field(...)
    description: str = Field(...)
    spec: Dict

    class Config:

        schema_extra = {
            'example': {
                'item_id': 1,
                'item_name': 'EPhone 2021',
                'description': 'A new 2021 EPhone model',
                'spec': {'RAM': '8Gb', 'CPU': 'Viking A'},
            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
