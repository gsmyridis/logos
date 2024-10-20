from os import PathLike
from typing import Union, NewType, Sequence

from llama_index.core.schema import BaseNode

Path = NewType("Path", Union[str, PathLike])
Nodes = Sequence[BaseNode]
