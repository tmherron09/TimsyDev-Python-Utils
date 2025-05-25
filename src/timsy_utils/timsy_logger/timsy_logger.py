import logging
from datetime import datetime
from multiprocessing import Queue

from . import (
    console_handler_factory,
    file_handler_factory,
    get_logger_initialized,
    HandlerFactory,
    set_logger_initialized,
    verify_log_folder,
    LoggingHandlerConfig,
    HandlerType,
    log_multiline
)

logger = logging.getLogger()


@verify_log_folder
def init_default_logger(logger_name: str = None):
    if get_logger_initialized():
        return
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    _initial_file_log(logger)
    HandlerFactory.add_default_root(logger)
    set_logger_initialized(True)


@verify_log_folder
def init_root_logger(console_handler_use_info_filter: bool = True, file_handler_use_info_filter: bool = False):
    """ Opinionated Default Root Logger """
    if get_logger_initialized():
        return
    init_logger = logging.getLogger()
    init_logger.setLevel(logging.DEBUG)
    _initial_file_log(init_logger)
    root_handlers = [
        LoggingHandlerConfig(HandlerType.FILE, log_level=logging.DEBUG,
                             use_info_filter=file_handler_use_info_filter),
        LoggingHandlerConfig(HandlerType.CONSOLE, log_level=logging.INFO,
                             use_info_filter=console_handler_use_info_filter)]
    HandlerFactory.add_handlers(init_logger, root_handlers)
    set_logger_initialized(True)


@verify_log_folder
def _initial_file_log(init_logger: logging.Logger):
    init_logger.name = init_logger.name if init_logger.name != 'root' else 'Root'
    entry_fh = logging.FileHandler('logs/timsy_app.log')
    entry_fh.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    entry_fh.setFormatter(log_formatter)
    init_logger.addHandler(entry_fh)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry_message = ["-------------------------",
                     f"{init_logger.name} Logger Initialized: {current_time}",
                     "-------------------------"]
    log_multiline(init_logger, 'DEBUG', entry_message)
    init_logger.removeHandler(entry_fh)


@verify_log_folder
def init_default_listener_logger(logger_name: str = "LoggingListenerProcess"):
    if get_logger_initialized():
        return
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    HandlerFactory.add_default_listener(logger)
    set_logger_initialized(True)


def init_default_ipc_logger(queue: Queue, process_name: str):
    if get_logger_initialized():
        return
    logger = logging.getLogger(process_name)
    logger.setLevel(logging.DEBUG)
    HandlerFactory.add_default_queue(logger, queue)
    set_logger_initialized(True)


@verify_log_folder
def init_handler_configs(handler_configs: LoggingHandlerConfig | list[LoggingHandlerConfig], logger_name: str = None,
                         log_level: int | str = logging.DEBUG, queue: Queue = None):
    if not isinstance(handler_configs, list):
        handler_configs = [handler_configs]
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    for handler_config in handler_configs:
        HandlerFactory.add_handler(logger, handler_config, queue)
    set_logger_initialized(True)


def setup_logger():
    class InfoFilter(logging.Filter):
        def filter(self, record):
            return record.levelno == logging.INFO

    logger.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fh = logging.FileHandler('logs/timsy_app.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(log_formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(log_formatter)
    ch.addFilter(InfoFilter())
    logger.addHandler(ch)


def init_root_logger():
    """ Opinionated Default Root Logger """
    # global TIMSY_LOGGER_INITIALIZED
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = file_handler_factory()
    ch = console_handler_factory(use_info_filter=True)

    entry_fh = logging.FileHandler('logs/timsy_app.log')
    entry_fh.setLevel(logging.DEBUG)
    logger.addHandler(entry_fh)
    logger.debug("-------------------------")
    logger.debug("Root Logger Initialized.")
    logger.debug("-------------------------")
    logger.removeHandler(entry_fh)
    logger.addHandler(fh)
    logger.addHandler(ch)
    set_logger_initialized(True)


def getLogger(name: str | None = None) -> logging.Logger:
    return logging.getLogger(name)
