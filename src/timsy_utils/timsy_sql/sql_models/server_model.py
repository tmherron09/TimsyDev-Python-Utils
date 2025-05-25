from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ServerModel:
    """
    Represents a SQL server, supporting multiple common names, a preferred common name, environment, and notes.
    """
    server_name: str
    environment: str
    common_names: List[str] = field(default_factory=list)
    preferred_common_name: Optional[str] = None
    notes: List['NoteModel'] = field(default_factory=list)

    def __post_init__(self):
        if self.common_names:
            if self.preferred_common_name is None:
                self.preferred_common_name = self.common_names[0]
        else:
            # If no common_names provided, use server_name as default
            self.common_names = [self.server_name]
            self.preferred_common_name = self.server_name

    def __str__(self) -> str:
        return (f"Server Common Name: {self.preferred_common_name}. "
                f"Server Name: {self.server_name}. "
                f"Environment: {self.environment}. "
                f"Notes: {self.notes}")

    def add_common_name(self, common_name: str) -> None:
        """Add a new common name to the server."""
        if common_name in self.common_names:
            raise ValueError(f"Common Name '{common_name}' already exists.")
        self.common_names.append(common_name)
        if self.preferred_common_name is None or self.preferred_common_name == '':
            self.preferred_common_name = common_name

    def select_preferred_common_name(self, common_name: str) -> None:
        """Set the preferred common name from the list of common names."""
        if common_name in self.common_names:
            self.preferred_common_name = common_name
        else:
            raise ValueError(f"Common Name '{common_name}' not found in common names.")

    @property
    def name(self) -> str:
        """Get the preferred common name in brackets."""
        return f"[{self.preferred_common_name}]"

    @property
    def env(self) -> str:
        """Get the environment in brackets."""
        return f"[{self.environment}]"

    @classmethod
    def load_dict(cls, dict_data: dict) -> 'ServerModel':
        """Create a ServerModel instance from a dictionary."""
        return cls(
            server_name=dict_data.get('server_name', ''),
            environment=dict_data.get('environment', ''),
            common_names=dict_data.get('common_names', []),
            preferred_common_name=dict_data.get('preferred_common_name'),
            notes=dict_data.get('notes', [])
        )

# Note: 'NoteModel' should be imported or defined elsewhere in your codebase.

if __name__ == "__main__":
    server_model = ServerModel(server_name="SQLServer1", environment="Production")
    print(server_model.name)
    server_model.add_common_name("ServerABC")
    print(server_model.name)

    print(server_model.env)
