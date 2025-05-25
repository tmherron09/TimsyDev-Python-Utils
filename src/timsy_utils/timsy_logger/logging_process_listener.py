from datetime import datetime
from multiprocessing import Process, Queue
from typing import Union

from . import (
    LoggingHandlerConfig,
    LoggingBroadcaster,
    init_root_logger,
    init_default_listener_logger,
    getLogger
)


class LoggingProcessListener:
    def __init__(self, log_queue: Union[Queue, None] = None, start_at_init: bool = True):
        self.process = None
        self._log_queue: Queue = log_queue or Queue()
        if start_at_init:
            self.start()

    def start(self) -> None:
        self.process = Process(target=self._listen, args=(self._log_queue,))
        self.process.start()

    def stop(self) -> None:
        self._log_queue.put(None)
        self.process.join()

    def is_alive(self) -> bool:
        return self.process.is_alive()

    def get_log_queue(self) -> Queue:
        if not self.process.is_alive():
            raise RuntimeError("The listener process is not running")
        return self._log_queue

    def broadcaster_factory(self, process_name: str = None, queue_handler: LoggingHandlerConfig = None):
        return LoggingBroadcaster.from_listener(self, process_name=process_name, queue_handler=queue_handler)

    @staticmethod
    def _listen(queue: Queue, process_name: str = None) -> None:
        """
        Listener function that receives logs from the queue and handles them with a single handler.
        This function should run in a dedicated process.
        """
        process_name = process_name or "LoggingListenerProcess"

        def _format_message(msg: str) -> str:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return f"{current_time} - {process_name} - INFO - {msg}"

        init_default_listener_logger(process_name)
        init_root_logger(console_handler_use_info_filter=False)

        listener_logger = getLogger(process_name)

        listener_logger.info(_format_message("Logging listener process started"))

        while True:
            record = queue.get()
            if record is None:
                listener_logger.info(_format_message("Logging listener process stopping"))
                break
            listener_logger.handle(record)


if __name__ == "__main__":
    listener = LoggingProcessListener()

    logging_broadcaster = listener.broadcaster_factory()

    logging_broadcaster.info("This is a test message")
    logging_broadcaster.error("This is an error message")
    logging_broadcaster.warning("This is a warning message")
    logging_broadcaster.debug("This is a debug message")
    logging_broadcaster.info("The Logger Listener Process is alive: %s", listener.is_alive())

    listener.stop()
