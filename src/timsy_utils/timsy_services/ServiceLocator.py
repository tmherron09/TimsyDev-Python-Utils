from . import _default_factories
from typing import Any, Callable, Dict

class ServiceLocator:
    """
    A registry for application-wide services, supporting registration, retrieval, and default factories.
    """
    _services: Dict[str, Any] = {}

    @classmethod
    def register(cls, name: str, service: Any = None, force_replace: bool = False) -> None:
        """
        Register a service by name. If service is None, use the default factory.
        If force_replace is False and the service exists, raises ValueError.
        """
        if name in cls._services and not force_replace:
            raise ValueError(f"Service '{name}' is already registered.")
        if service is None:
            if name not in _default_factories:
                raise ValueError(f"No default factory for service '{name}'")
            service = _default_factories[name]()
        cls._services[name] = service

    @classmethod
    def register_default(cls, name: str, force_replace: bool = False) -> None:
        """
        Register a service using its default factory.
        """
        cls.register(name, service=None, force_replace=force_replace)

    @classmethod
    def register_defaults(cls, force_replace: bool = False) -> None:
        """
        Register all default services. Optionally force replace existing ones.
        """
        for name in _default_factories:
            if name not in cls._services or force_replace:
                cls.register_default(name, force_replace=force_replace)

    @classmethod
    def unregister(cls, name: str) -> None:
        """
        Unregister a service by name.
        """
        cls._services.pop(name, None)

    @classmethod
    def unregister_all(cls) -> None:
        """
        Unregister all services.
        """
        cls._services.clear()

    @classmethod
    def get(cls, name: str) -> Any:
        """
        Retrieve a registered service by name, or None if not found.
        """
        return cls._services.get(name, None)

    @classmethod
    def list_services(cls):
        """
        List all registered service names.
        """
        return list(cls._services.keys())

