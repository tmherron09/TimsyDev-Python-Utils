import configparser
from pathlib import Path

import timsy_utils.timsy_logger as logging

CONFIG_FILE = 'config.ini'
# module_logger = logging.getLogger(f'MainAppLogger.{__name__}')
module_logger = logging.getLogger(__name__)


def config_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as ke:
            module_logger.warning(f'{type(ke).__name__}: {ke}')
            return None
        except configparser.NoOptionError as noe:
            module_logger.warning(f'{type(noe).__name__}: {noe}')
            return None
        except FileNotFoundError as fnfe:
            module_logger.error(f'{type(fnfe).__name__}: {fnfe}')
            raise fnfe
        except Exception as e:
            module_logger.warning(f'Unhandled Exception - {type(e).__name__}: {e}')
            raise e

    return wrapper


def override_default_config_file(config_file: str):
    global CONFIG_FILE
    CONFIG_FILE = config_file


def reset_default_config_file():
    """ Reset the default hard coded config.ini. """
    global CONFIG_FILE
    cp = configparser.ConfigParser()
    cp.default_section = 'DEFAULT'
    cp.set('DEFAULT', 'insertDefaultHere', 'TODO')
    cp.set('DEFAULT', 'loggerName', 'TimsyAppLogger')
    cp.set('DEFAULT', 'loggerFileName', 'logs/timsy_app.log')
    cp.set('DEFAULT', 'testIndexNumber', '86')
    with open(CONFIG_FILE, 'w') as f:
        cp.write(f)


@config_error_handler
def check_config_file(config_file: str = CONFIG_FILE):
    # Check if the config file exists
    if not Path(config_file).exists():
        raise FileNotFoundError(f"Config file '{config_file}' not found.")
    # Check reader can open config file
    with open(config_file, 'r') as f:
        return True


class Config:
    def __init__(self, config_file: str = CONFIG_FILE):
        try:
            check_config_file(config_file)
        except FileNotFoundError as fnfe:
            reset_default_config_file()
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.logger = module_logger

    @config_error_handler
    def get(self, section='DEFAULT', key=''):
        module_logger.info(f'Getting {key} from {section}')
        return self.config[section][key]

    @config_error_handler
    def get_int(self, section='DEFAULT', key=''):
        return self.config.getint(section, key)

    @config_error_handler
    def get_float(self, section='DEFAULT', key=''):
        return self.config.getfloat(section, key)

    @config_error_handler
    def get_boolean(self, section='DEFAULT', key=''):
        return self.config.getboolean(section, key)

    @config_error_handler
    def get_list(self, section='DEFAULT', key=''):
        return self.config[section][key].split(',')

    @config_error_handler
    def get_section(self, section='DEFAULT'):
        return dict(self.config[section])

    @config_error_handler
    def get_sections(self):
        return self.config.sections()

    def set(self, section: str, key: str, value: str):
        """Set a value in the config and update the file."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, value)
        with open(self.config_file, 'w') as f:
            self.config.write(f)
        self.logger.info(f'Set {key} in {section} to {value}')

    def save(self, file_path: str = None):
        """Save the current config to a file."""
        path = file_path or self.config_file
        with open(path, 'w') as f:
            self.config.write(f)
        self.logger.info(f'Config saved to {path}')

    def reload(self):
        """Reload the config from the file."""
        self.config.read(self.config_file)
        self.logger.info(f'Config reloaded from {self.config_file}')

    def has_option(self, section: str, key: str) -> bool:
        """Check if a section/key exists in the config."""
        return self.config.has_option(section, key)

    def has_section(self, section: str) -> bool:
        """Check if a section exists in the config."""
        return self.config.has_section(section)

    def remove_option(self, section: str, key: str):
        """Remove a key from a section and update the file."""
        removed = self.config.remove_option(section, key)
        with open(self.config_file, 'w') as f:
            self.config.write(f)
        self.logger.info(f'Removed {key} from {section}')
        return removed

    def remove_section(self, section: str):
        """Remove a section from the config and update the file."""
        removed = self.config.remove_section(section)
        with open(self.config_file, 'w') as f:
            self.config.write(f)
        self.logger.info(f'Removed section {section}')
        return removed

    def as_dict(self) -> dict:
        """Return the entire config as a dictionary."""
        return {section: dict(self.config[section]) for section in self.config.sections()}

    def get_with_env(self, section='DEFAULT', key='', env_var=None):
        """Get a config value, optionally overridden by an environment variable."""
        import os
        if env_var and env_var in os.environ:
            self.logger.info(f'Using environment variable {env_var} for {key}')
            return os.environ[env_var]
        return self.get(section, key)


if __name__ == '__main__':
    config = Config(config_file='../config.ini')
    print(config.get('DEFAULT', 'applicationIcon'))
    print(config.get('DEFAULT', 'sqlFolder'))
    print(config.get_int('DEFAULT', 'sqlCount'))
    print(config.get_float('DEFAULT', 'sqlFloat'))
    print(config.get_boolean('DEFAULT', 'sqlBoolean'))
    print(config.get_list('DEFAULT', 'emptyList'))
    print(config.get_list('DEFAULT', 'applicationIcon'))
    print(config.get_section('EMPTY'))
    print(config.get_sections())
