from multiprocessing import Queue
from typing import TYPE_CHECKING

from . import LoggingHandlerConfig, init_handler_configs, init_default_ipc_logger, getLogger

if TYPE_CHECKING:
    from . import LoggingProcessListener

class LoggingBroadcaster:
    def __init__(self, log_queue: Queue, process_name: str = None, queue_handler: LoggingHandlerConfig = None):
        self._log_queue = log_queue
        process_name = process_name or f"{__name__}"

        if queue_handler:
            init_handler_configs(queue_handler, process_name=process_name, log_level=queue_handler.log_level,
                                 queue=self._log_queue)
        else:
            init_default_ipc_logger(self._log_queue, process_name=process_name)

        self._logger = getLogger(process_name)

    @classmethod
    def from_listener(cls, log_listener: 'LoggingProcessListener', process_name: str = None,
                      queue_handler: LoggingHandlerConfig = None):
        return cls(log_listener.get_log_queue(), process_name=process_name, queue_handler=queue_handler)

    def info(self, msg: str, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def debug(self, msg: str, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)

    def exception(self, msg: str, *args, **kwargs):
        self._logger.exception(msg, *args, **kwargs)
