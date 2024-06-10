from typing import TypeVar, Generic, Union, Dict
from pydantic.generics import GenericModel
T = TypeVar('T')

class ResponseModel(GenericModel, Generic[T]):

    message: str
    data: Union[T, Dict, None]