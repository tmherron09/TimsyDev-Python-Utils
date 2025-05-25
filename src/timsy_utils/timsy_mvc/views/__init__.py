"""timsy_mvc.views package

This package contains view classes for the MVC pattern, including:
- HomeView: The main home screen view.
- Root: The main application window.
- AbstractViewManager: Base class for managing views.

Usage:
    from timsy_mvc.views import HomeView, Root, AbstractViewManager
"""

from .main import (
    AbstractViewManager
)

from .home import (
    HomeView
)

from .root import (
    Root
)

__all__ = ["HomeView", "Root", "AbstractViewManager"]
