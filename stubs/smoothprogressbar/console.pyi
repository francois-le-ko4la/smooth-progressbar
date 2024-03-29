from smoothprogressbar.__config__ import Theme as Theme

class Console:
    def __init__(self) -> None: ...
    @property
    def size(self) -> int: ...
    def addmsg(self, msg: str) -> Console: ...
    def emptyline(self) -> Console: ...
    def addtab(self) -> Console: ...
    def goback(self) -> Console: ...
    def newline(self) -> Console: ...
    def print(self) -> None: ...
