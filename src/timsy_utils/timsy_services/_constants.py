from . import ConfigService, LoggerService

_default_factories = {
    "ConfigService": ConfigService.default_factory,
    "LoggerService": LoggerService.default_factory
}