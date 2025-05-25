from _constants import _default_factories


class ServiceLocator:
    _services = {}

    @classmethod
    def register(cls, name, service, force_replace=False):
        if not name in cls._services or force_replace:
            cls._services[name] = service or _default_factories[name]
        else:
            raise ValueError(f"Service {name} already registered")

    @classmethod
    def register_service_default(cls, name, force_replace=False):
        if not name in _default_factories:
            raise ValueError(f"Default Service {name} not found")
        if not name in cls._services or force_replace:
            cls.register(name, service=None, force_replace=force_replace)

    @classmethod
    def register_defaults(cls, force_replace=False):
        for name, default_factory in _default_factories.items():
            if not name in cls._services or force_replace:
                cls._services[name] = default_factory