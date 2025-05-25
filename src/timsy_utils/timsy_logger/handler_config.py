import logging
from multiprocessing import Queue
from typing import Union
from . import  HandlerType

class LoggingHandlerConfig:
    def __init__(self, handler_type: HandlerType, log_level=logging.DEBUG, log_formatter=None, log_filter=None,
                 use_info_filter=False, file_name='timsy_app.log', queue: Union[Queue, None] = None):
        self.handler_type = handler_type
        self.log_level = log_level
        self.log_formatter = log_formatter
        self.log_filter = log_filter
        self.file_name = file_name
        self.use_info_filter = use_info_filter
        self.queue = queue

    @classmethod
    def default_console(cls):
        return cls(HandlerType.CONSOLE, log_level=logging.INFO, use_info_filter=True)

    @classmethod
    def default_file(cls):
        return cls(HandlerType.FILE, log_level=logging.DEBUG, use_info_filter=False)

    @classmethod
    def default_root(cls):
        return [
            cls(HandlerType.FILE, log_level=logging.DEBUG),
            cls(HandlerType.CONSOLE, log_level=logging.INFO, use_info_filter=True)]

    @classmethod
    def default_listener(cls):
        return [
            cls(HandlerType.FILE, log_level=logging.DEBUG, log_formatter=logging.Formatter('%(message)s'),
                use_info_filter=False),
            cls(HandlerType.CONSOLE, log_level=logging.INFO, log_formatter=logging.Formatter('%(message)s'),
                use_info_filter=True)]

    @classmethod
    def default_queue(cls, queue: Queue):
        return cls(HandlerType.QUEUE, log_level=logging.DEBUG, queue=queue)
