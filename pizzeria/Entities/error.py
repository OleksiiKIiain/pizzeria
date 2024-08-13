from pydantic import BaseModel


class ErrorResult(BaseModel):
    message : str