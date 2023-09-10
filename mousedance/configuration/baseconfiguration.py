
from yaml import FullLoader
from yaml import load

from typing import Dict
from typing import TypeVar

T = TypeVar("T")

class BaseConfiguration(Dict[str, T]):
    
    def __init__(self, path: str):
        with open(file = path, mode = "r") as descriptor:
            super().__init__(load(descriptor, FullLoader))