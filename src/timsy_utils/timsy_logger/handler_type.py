from enum import Enum

class HandlerType(Enum):
    CONSOLE = "console"
    FILE = "file"
    QUEUE = "queue"
