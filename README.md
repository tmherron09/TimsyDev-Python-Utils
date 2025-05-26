# Timsy Utils

A collection of utility modules for TimsyDev projects, organized as a Python package. This library provides reusable components for configuration, logging, HTTP, CSV, SQL, and more.

## Features
- Modular utilities for common tasks
- Organized by functionality (config, logger, SQL, etc.)
- Designed for easy integration into your projects

## Installation

Clone this repository and install in editable mode:

```bash
pip install -e .
```

This allows you to edit the code in `src/timsy_utils` and have changes reflected immediately.

## Usage Example

Import and use modules in your Python code:

```python
from timsy_utils.timsy_config import config
from timsy_utils.timsy_logger import timsy_logger

config_data = config.load_config('config.ini')
logger = timsy_logger.get_logger()
logger.info("Timsy Utils is ready!")
```

## Project Structure

```
TimsyUtils/
├── pyproject.toml                # Project metadata and build configuration
├── README.md                     # Project documentation
└── src/
    └── timsy_utils/
        ├── timsy_appdata/
        │   ├── __init__.py
        │   └── timsy_appdata.py
        ├── timsy_config/
        │   ├── __init__.py
        │   └── config.py
        ├── timsy_csv/
        │   ├── __init__.py
        │   └── timsy_csv_misc.py
        ├── timsy_http/
        │   └── __init__.py
        ├── timsy_json/
        │   ├── __init__.py
        │   └── JsonService.py
        ├── timsy_logger/
        │   ├── __init__.py
        │   ├── _constants.py
        │   ├── handler_config.py
        │   ├── handler_factory.py
        │   ├── handler_type.py
        │   ├── logging_broadcaster.py
        │   ├── logging_misc.py
        │   └── timsy_logger.py
        ├── timsy_markdown_generator/
        │   ├── __init__.py
        │   └── dynamo_md_generator.py
        ├── timsy_misc/
        │   ├── __init__.py
        │   └── class_file_generator.py
        ├── timsy_mvc/
        │   ├── main.py
        │   ├── readme.md
        │   ├── step_by_step_tutorial.md
        │   ├── controllers/
        │   │   ├── home.py
        │   │   └── main.py
        │   ├── models/
        │   │   ├── home.py
        │   │   └── main.py
        │   ├── timsy_mvc_template/
        │   │   ├── controller.py
        │   │   ├── main.py
        │   │   ├── model.py
        │   │   └── view.py
        │   └── views/
        │       ├── home.py
        │       ├── main.py
        │       └── root.py
        ├── timsy_service_locator/
        │   ├── __init__.py
        │   ├── _constants.py
        │   └── service_locator.py
        ├── timsy_services/
        │   ├── __init__.py
        │   ├── _constants.py
        │   ├── ConfigService.py
        │   ├── HttpService.py
        │   └── ServiceLocator.py
        ├── timsy_sql/
        │   ├── __init__.py
        │   ├── query_model.py
        │   ├── sql_builder.py
        │   ├── sql_conn.py
        │   ├── sql_file.py
        │   ├── SqlServerConnection.py
        │   ├── timsy_alchemy.py
        │   ├── timsy_sql_util.py
        │   ├── misc_scripts/
        │   │   ├── build_string_agg.sql
        │   │   ├── example_basic_query.sql
        │   │   ├── example_query_format_params.sql
        │   │   ├── example_query_with_params.sql
        │   │   └── show_play.sql
        │   └── sql_models/
        │       ├── __init__.py
        │       ├── column_entry.py
        │       ├── column_instance.py
        │       ├── database_model.py
        │       ├── join_table.py
        │       ├── join_types.py
        │       ├── note_model.py
        │       ├── on_clause.py
        │       ├── proc.py
        │       ├── server_model.py
        │       ├── sql_column_type.py
        │       ├── sql_model_helpers.py
        │       ├── table_info.py
        │       └── table_relationship.py
        ├── timsy_tcl/
        │   ├── __init__.py
        │   ├── main.py
        │   ├── root_tk_call_proc_guide.md
        │   ├── style_01.tcl
        │   ├── tcl_file_guide.md
        │   ├── tcl_label_reference.md
        │   └── theme_01.tcl
        └── timsy_tk/
            ├── __init__.py
            ├── tk_constant_enums.py
            ├── assets/
            │   ├── __init__.py
            │   └── python_logo.ico
            ├── components/
            │   ├── __init__.py
            │   ├── app_frame.py
            │   ├── image_attribution
            │   └── image_button - Copy.png
            └── unorganized/
```

## Configuration

Some modules (like `timsy_config`) expect a `config.ini` file. Place your `config.ini` in the project root or specify its path when loading configuration.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

MIT License

### Note -e git+https://github.com/tmherron09/TimsyDev-Python-Utils.git@273707c5764721dfe713888d392a6ae9517c5a97#egg=timsy_utils
### pip install git+https://github.com/tmherron09/TimsyDev-Python-Utils.git
