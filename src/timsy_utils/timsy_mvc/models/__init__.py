"""timsy_mvc.models package

This package contains model classes for the MVC pattern, including:
- HomeModel: The model for the home view.
- AbstractModel: Base class for models.

Usage:
    from timsy_mvc.models import HomeModel, AbstractModel
"""

from .main import (
    AbstractModel
)

from .home import (
    HomeModel,
)

__all__ = ["HomeModel", "AbstractModel"]

