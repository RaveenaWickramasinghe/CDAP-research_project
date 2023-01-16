from array import ArrayType, array
from multiprocessing.dummy import Array
from typing import Any, List
from pydantic import BaseModel

class GrammarModel(BaseModel):
    grammar: str
