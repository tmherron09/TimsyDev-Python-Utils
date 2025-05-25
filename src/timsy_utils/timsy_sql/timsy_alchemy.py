import configparser
from typing import Sequence, List, Union, Callable, Literal
from sqlalchemy import create_engine, text, Column, Integer, String, MetaData, Table
from sqlalchemy.engine import CursorResult, Engine
from sqlalchemy.orm import sessionmaker, Session, Query, declarative_base
from sqlalchemy.schema import CreateTable
import pandas as pd

# Debug print flag and function
_IS_DEBUG_PRINT = False
def _debug_print(*args, **kwargs):
    if _IS_DEBUG_PRINT:
        print(*args, **kwargs)

class TimsySqlAlchemyUtil:
    """
    Flexible SQLAlchemy utility for engine/session management, query execution, ORM helpers, and config management.
    """
    Base = declarative_base()
    SqlAlchemyUtil = None  # Class-level default instance

    def __init__(self, config_section: str = 'DEFAULT', set_default: bool = False):
        self.config = configparser.ConfigParser()
        self.config_section = config_section
        self.config.read('config.ini')
        section = self.config[config_section]
        self.server = section['server']
        self.database = section['database']
        # Prefer section's trusted_connection, fallback to DEFAULT, then 'yes'
        self.trusted_connection = (
            section.get('trusted_connection')
            or self.config['DEFAULT'].get('trusted_connection', 'yes')
        ).lower() in ['yes', 'true', '1']
        if self.trusted_connection:
            connection_string = f"mssql+pyodbc://{self.server}/{self.database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
        else:
            self.username = section.get('username') or self.config['DEFAULT'].get('username')
            self.password = section.get('password') or self.config['DEFAULT'].get('password')
            connection_string = f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}"
        self.engine: Engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        if set_default:
            TimsySqlAlchemyUtil.SqlAlchemyUtil = self

    def execute(self, query_func: Callable[[Session], any], is_cursor_result: bool = True, commit: bool = False):
        """
        Execute a query function with a session. Optionally commit.
        """
        session = self.Session()
        try:
            _debug_print('Executing query_func in TimsySqlAlchemyUtil...')
            result = query_func(session)
            if commit:
                session.commit()
            if not is_cursor_result:
                return result
            # If result is a SQLAlchemy result, try .all()
            if hasattr(result, 'all'):
                return result.all()
            return result
        except Exception as e:
            if commit:
                session.rollback()
            raise e
        finally:
            session.close()

    def run_sql_file(self, sql_file_path: str) -> CursorResult:
        def query_func(session):
            with open(sql_file_path, 'r') as file:
                sql_query = file.read()
            return session.execute(text(sql_query))
        return self.execute(query_func)

    def query_all_tables(self, schema: str = 'Production', table_name: str = 'Product') -> Sequence:
        def query_func(session: Session) -> List:
            metadata = MetaData(schema=schema)
            table_data: Table = Table(table_name, metadata, autoload_with=self.engine)
            _debug_print("|***********\tSys_tables\t***********|", table_data)
            query: Query = session.query(table_data)
            _debug_print("|***********\tQuery\t***********|", query)
            return query.all()
        return self.execute(query_func, is_cursor_result=False)

    def query_create_table_stmt(self, table_name: str, schema: str = 'Production') -> str:
        metadata = MetaData()
        table = Table(table_name, metadata, autoload_with=self.engine, schema=schema)
        return str(CreateTable(table))

    @staticmethod
    def to_dataframe(query_result) -> pd.DataFrame:
        """Convert a SQLAlchemy query result to a pandas DataFrame."""
        if isinstance(query_result, (list, Sequence)) and query_result and hasattr(query_result[0], '__table__'):
            # ORM objects
            return pd.DataFrame([row.__dict__ for row in query_result])
        elif hasattr(query_result, 'fetchall'):
            # Raw cursor
            return pd.DataFrame(query_result.fetchall(), columns=query_result.keys())
        return pd.DataFrame(query_result)

    def pandas_test(self, table: str = 'Person', schema: str = 'Person', index_col: str = 'BusinessEntityID', chunksize: int = 10):
        df = pd.read_sql_table(table, self.engine, schema=schema, index_col=index_col, chunksize=chunksize)
        dfe = enumerate(df)
        _debug_print(next(dfe))
        _debug_print(next(dfe))
        _debug_print(next(dfe))

    @staticmethod
    def add_new_config_section(config_section, server, database, trusted_connection: Literal['yes','no'], server_common_name: str = '', username: str = '', password: str = ''):
        config = configparser.ConfigParser()
        config.read('config.ini')
        config[config_section] = {
            'server': server,
            'ServerCommonName': server_common_name,
            'database': database,
            'trusted_connection': trusted_connection,
            'username': username,
            'password': password
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    @staticmethod
    def remove_config_section(config_section):
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.remove_section(config_section)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

# Expose useful SQLAlchemy objects for convenience
__all__ = [
    'TimsySqlAlchemyUtil', 'text', 'Engine', 'CursorResult', 'Session', 'Query', 'declarative_base',
    'Column', 'Integer', 'String', 'MetaData', 'Table', 'CreateTable', 'pd', '_IS_DEBUG_PRINT', '_debug_print'
]

if __name__ == "__main__":
    util = TimsySqlAlchemyUtil(set_default=True)
    print(util.query_create_table_stmt('Product'))
    # util.pandas_test()
    # util.run_sql_file('scripts/example_basic_query.sql')
    # util.query_all_tables()
