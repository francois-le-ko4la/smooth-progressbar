from _typeshed import Incomplete
from smoothprogressbar.__config__ import Theme as Theme
from smoothprogressbar.consolestring import ConsoleString as ConsoleString

class ConsoleProgress(ConsoleString):
    tag_beg: Incomplete
    tag_end: Incomplete
    def __init__(self, tag_beg: str = ..., tag_end: str = ...) -> None: ...
    max_size: Incomplete
    text: Incomplete
    def update(self, size: int, ratio: float) -> ConsoleProgress: ...
