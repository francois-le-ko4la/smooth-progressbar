from _typeshed import Incomplete
from smoothprogressbar.__config__ import Theme as Theme
from smoothprogressbar.consoleprogress import ConsoleProgress as ConsoleProgress
from smoothprogressbar.consolestring import ConsoleString as ConsoleString
from smoothprogressbar.percent import Percent as Percent

class ConsolePrgBr:
    progress_label: str
    size_widgt_label_label: Incomplete
    size_widgt_percent: int
    def __init__(self, enable_elapse: bool = ..., enable_msg: bool = ..., debug: bool = ...) -> None: ...
    def update(self, size: int, percent: Percent, msg: str = ..., elapse: str = ...) -> ConsolePrgBr: ...
    def get(self) -> str: ...
