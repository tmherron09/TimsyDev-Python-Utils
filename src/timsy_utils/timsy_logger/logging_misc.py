import logging
import os
from multiprocessing import Queue
import logging.handlers

def verify_log_folder(func):
    """
    A decorator that ensures the existence of a 'logs' directory before executing the decorated function.

    This decorator checks if a directory named 'logs' exists in the current working directory. If it does not exist,
    the decorator creates the directory. After ensuring the directory's existence, it calls the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function that includes the directory verification step.
    """

    def wrapper(*args, **kwargs):
        if not os.path.isdir("logs"):
            os.makedirs("logs", exist_ok=True)
        return func(*args, **kwargs)

    return wrapper


class InfoFilter(logging.Filter):
    """
    A logging filter that only allows INFO level log records to pass through.

    This filter can be added to a logging handler to ensure that only log records
    with a level of INFO are processed by that handler. Nothing Higher or Lower.

    Methods:
        filter(record): Determines if the specified log record should be processed.
    """

    def filter(self, record):
        """
        Determines if the specified log record should be processed.

        Args:
            record (logging.LogRecord): The log record to be filtered.

        Returns:
            bool: True if the log record's level is INFO, False otherwise.
        """
        return record.levelno == logging.INFO


def console_handler_factory(log_level: int = logging.INFO,
                            log_formatter: logging.Formatter = None,
                            log_filter: logging.Filter = None,
                            use_info_filter: bool = False) -> logging.Handler:
    """
    Creates a console logging handler with the specified log level, formatter, and filter.

    Args:
        log_level (int): The logging level for the handler. Default is logging.INFO.
        log_formatter (logging.Formatter): The formatter to use for the handler. Default is a standard formatter.
        log_filter (logging.Filter): The filter to apply to the handler. Default is None.
        use_info_filter (bool): Whether to use the InfoFilter. Default is False.

    Returns:
    logging.Handler: The configured console logging handler.
    """
    log_formatter = log_formatter if log_formatter else logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - '
                                                                          '%(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(log_formatter)
    log_filter = log_filter if log_filter else (InfoFilter() if use_info_filter else None)
    if log_filter:
        ch.addFilter(log_filter)
    return ch


@verify_log_folder
def file_handler_factory(log_level: int = logging.DEBUG,
                         log_formatter: logging.Formatter = None,
                         log_filter: logging.Filter = None,
                         file_name: str = 'timsy_app.log',
                         use_info_filter: bool = False) -> logging.Handler:
    log_formatter = log_formatter if log_formatter else logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - '
                                                                          '%(message)s')
    # log_formatter = log_formatter if log_formatter else logging.Formatter('%(message)s')
    fh = logging.FileHandler(f'logs/{file_name}')
    fh.setLevel(log_level)
    fh.setFormatter(log_formatter)
    log_filter = log_filter if log_filter else (InfoFilter() if use_info_filter else None)
    if log_filter:
        fh.addFilter(log_filter)
    return fh


def queue_handler_factory(queue: Queue, log_level: int = logging.DEBUG, log_formatter: logging.Formatter = None,
                          log_filter: logging.Filter = None, use_info_filter: bool = False) -> logging.Handler:
    log_formatter = log_formatter if log_formatter else logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - '
                                                                          '%(message)s')
    qh = logging.handlers.QueueHandler(queue)
    qh.setLevel(log_level)
    qh.setFormatter(log_formatter)
    log_filter = log_filter if log_filter else (InfoFilter() if use_info_filter else None)
    if log_filter:
        qh.addFilter(log_filter)
    return qh


def print_logger_details(logger: logging.Logger, display_method=print()):
    """
    Print the details of a logger, including its name, level, handlers, and filters.
    :param display_method: Callback function to display the output. Default is print.
    :param logger: The logger to print details for.
    """
    # Print the logger's name, level, handlers, and filters
    display_method(f"Logger Name: {logger.name}")
    display_method(f"Logger Level: {logging.getLevelName(logger.level)}")
    display_method(f"Logger Handlers: {len(logger.handlers)}")
    display_method(f"Logger Filters: {len(logger.filters)}")

    # Iterate through each handler to print its configuration
    for i, handler in enumerate(logger.handlers, start=1):
        display_method(f"\nHandler {i}:")
        display_method(f"    Type: {type(handler).__name__}")
        display_method(f"    Level: {logging.getLevelName(handler.level)}")
        display_method(f"    Formatter: {handler.formatter}")
        display_method(f"    Filters: {len(handler.filters)}")
        for j, filter in enumerate(handler.filters, start=1):
            display_method(f"        Filter {j}: {type(filter).__name__}")


def log_multiline(logger: logging.Logger, log_level: int | str, lines: list[str]):
    """
    Log multiple lines of text to the specified logger at the specified log level.
    :param logger: The logger to write the log messages to.
    :param log_level: The logging level to use for the messages.
    :param lines: A list of strings to log as individual lines.
    """
    level = log_level if isinstance(log_level, int) else logging.getLevelName(log_level.upper())
    try:
        for line in lines:
            logger.log(level, line)
    except TypeError:
        logger.error(f"Error logging multiline - Level: {log_level}\n Intended lines: {lines}")



if __name__ == '__main__':
    logger = logging.getLogger('MiscLoggingTest')
    logger.setLevel(logging.DEBUG)
    console_handler = console_handler_factory()
    logger.addHandler(console_handler)
    print_logger_details(logger, logger.info)

    _main_logger = logging.getLogger('MiscLoggingTest')
    _main_logger.setLevel(logging.DEBUG)
    console_handler = console_handler_factory()
    _main_logger.addHandler(console_handler)
    print_logger_details(_main_logger, _main_logger.info)