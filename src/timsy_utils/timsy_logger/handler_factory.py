import logging
from multiprocessing import Queue
from typing import Union

from . import LoggingHandlerConfig, HandlerType, console_handler_factory, file_handler_factory, queue_handler_factory


# TODO: Refactor into Functions to allow for explicit imports,
#  for now easier to import as a whole while experimenting.

class HandlerFactory:
    @staticmethod
    def build(config: LoggingHandlerConfig, queue: Queue = None) -> logging.Handler:

        if config.handler_type == HandlerType.CONSOLE:
            return HandlerFactory._console(config)
        elif config.handler_type == HandlerType.FILE:
            return HandlerFactory._file(config)
        elif config.handler_type == HandlerType.QUEUE:
            return HandlerFactory._queue(config, queue)
        else:
            raise ValueError('Invalid handler type')

    @staticmethod
    def build_all(configs: list[LoggingHandlerConfig], queue: Queue = None) -> list[logging.Handler]:
        return [HandlerFactory.build(config, queue) for config in configs]

    # Build default handlers methods

    @staticmethod
    def build_default_console() -> logging.Handler:
        return HandlerFactory._console(LoggingHandlerConfig.default_console())

    @staticmethod
    def build_default_file() -> logging.Handler:
        return HandlerFactory._file(LoggingHandlerConfig.default_file())

    @staticmethod
    def build_default_root() -> list[logging.Handler]:
        return HandlerFactory.build_all(LoggingHandlerConfig.default_root())

    @staticmethod
    def build_default_listener() -> list[logging.Handler]:
        return HandlerFactory.build_all(LoggingHandlerConfig.default_listener())

    @staticmethod
    def build_default_queue(queue: Queue) -> logging.Handler:
        return HandlerFactory._queue(LoggingHandlerConfig.default_queue(queue), queue)

    # Add handlers to logger methods

    @staticmethod
    def add_handler(logger: logging.Logger, config: LoggingHandlerConfig, queue: Queue = None, propagate: bool = None):
        logger.propagate = propagate if propagate is not None else config.handler_type != HandlerType.QUEUE
        logger.addHandler(HandlerFactory.build(config, queue))

    @staticmethod
    def add_handlers(logger: logging.Logger, configs: list[LoggingHandlerConfig], queue: Queue = None,
                     propagate: bool = None):
        for config in configs:
            HandlerFactory.add_handler(logger, config, queue, propagate)

    # Add default handlers to logger methods

    @staticmethod
    def add_default_console(logger: logging.Logger):
        logger.addHandler(HandlerFactory.build_default_console())

    @staticmethod
    def add_default_file(logger: logging.Logger):
        logger.addHandler(HandlerFactory.build_default_file())

    @staticmethod
    def add_default_root(logger: logging.Logger):
        for handler in HandlerFactory.build_default_root():
            logger.addHandler(handler)

    @staticmethod
    def add_default_listener(logger: logging.Logger):
        for handler in HandlerFactory.build_default_listener():
            logger.addHandler(handler)

    @staticmethod
    def add_default_queue(logger: logging.Logger, queue: Queue):
        logger.propagate = False
        logger.addHandler(HandlerFactory.build_default_queue(queue))

    # Handler Factory methods

    @staticmethod
    def _console(config: LoggingHandlerConfig) -> logging.Handler:
        return console_handler_factory(config.log_level, config.log_formatter,
                                       config.log_filter, config.use_info_filter)

    @staticmethod
    def _file(config: LoggingHandlerConfig) -> logging.Handler:
        return file_handler_factory(config.log_level, config.log_formatter,
                                    config.log_filter, config.file_name,
                                    config.use_info_filter)

    @staticmethod
    def _queue(config: LoggingHandlerConfig, queue: Union[Queue, None] = None) -> logging.Handler:
        if not config.queue and not queue:
            raise ValueError('Queue is required for queue handler')
        elif queue:
            config.queue = queue
        return queue_handler_factory(config.queue, config.log_level,
                                     config.log_formatter, config.log_filter,
                                     config.use_info_filter)
