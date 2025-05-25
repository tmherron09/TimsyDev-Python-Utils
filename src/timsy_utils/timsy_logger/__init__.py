import os

# check if directory "logs" exists
if not os.path.isdir("logs"):
    os.makedirs("logs", exist_ok=True)

from .handler_type import (
    HandlerType
)
from .handler_config import (
    LoggingHandlerConfig
)

from .handler_factory import (
    HandlerFactory
)

from ._constants import (
    get_logger_initialized,
    set_logger_initialized
)

from .logging_misc import (
    InfoFilter,
    console_handler_factory,
    file_handler_factory,
    log_multiline,
    verify_log_folder,
    print_logger_details,
    queue_handler_factory,
)

from .timsy_logger import (
    init_root_logger,
    getLogger,
    init_handler_configs,
    init_default_ipc_logger,
    init_default_listener_logger
)

from .logging_broadcaster import (
    LoggingBroadcaster
)

init_root_logger()
