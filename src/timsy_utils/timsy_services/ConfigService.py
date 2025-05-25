

class ConfigService:
    def __init__(self, config=None):
        self.settings = {"theme": "light", "version": "1.0"}
        self.config = config or Config()

    @classmethod
    def default_factory(cls):
        return cls()

    def get_setting(self, key, section: str = 'DEFAULT'):
        return self.config.get(section, key)

    def get_int_setting(self, key, section: str = 'DEFAULT') -> int:
        return self.config.get_int(section, key)

    def get_float_setting(self, key, section: str = 'DEFAULT') -> float:
        return self.config.get_float(section, key)

    def get_boolean_setting(self, key, section: str = 'DEFAULT') -> bool:
        return self.config.get_boolean(section, key)

    def get_list_setting(self, key, section: str = 'DEFAULT') -> list:
        return self.config.get_list(section, key)

    def get_section_setting(self, section: str = 'DEFAULT') -> dict:
        return self.config.get_section(section)

    def get_sections_setting(self) -> list:
        return self.config.get_sections()