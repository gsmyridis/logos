from os import PathLike
from typing import Union, NewType

Path = NewType("Path", Union[str, PathLike])
