import configparser
from typing import List, Optional, Callable
import pyodbc
import pandas as pd
import html

# --- PyODBC/Pandas-based SQL Utilities ---
class TableInfo:
    """
    Simple model for table metadata. Accepts any row tuple and stores as attributes.
    """
    def __init__(self, *args):
        for idx, value in enumerate(args):
            setattr(self, f'col{idx}', value)
    def __repr__(self):
        return f"TableInfo({', '.join(f'{k}={v}' for k, v in self.__dict__.items())})"

class TimsySqlUtil:
    def __init__(self, config_section: str = 'DEFAULT'):
        self.config = configparser.ConfigParser()
        self.config_section = config_section
        self.config.read('config.ini')
        self.server = self.config[self.config_section]['server']
        self.database = self.config[self.config_section]['database']
        self.trusted_connection = self.config[self.config_section]['trusted_connection']
        self.conn: Optional[pyodbc.Connection] = None

    def open_connection(self, database: Optional[str] = None):
        if database is not None:
            self.database = database
        self.conn = pyodbc.connect(
            f'DRIVER=ODBC Driver 17 for SQL Server;'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'Trusted_Connection={self.trusted_connection}'
        )
        return self.conn

    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def update_server(self, server: str):
        self.server = server

    def execute_query(self, query_func: Callable, database: Optional[str] = None):
        self.open_connection(database)
        try:
            result = query_func(self.conn)
            return result
        finally:
            self.close_connection()

    @staticmethod
    def read_sql_file(file_path: str) -> str:
        with open(file_path, 'r') as file:
            sql_query = file.read().strip()
        return sql_query

    def read_sql_to_df(self, file_path: str, query_params: Optional[List] = None, database: Optional[str] = None) -> pd.DataFrame:
        sql_query = self.read_sql_file(file_path)
        conn = self.open_connection(database)
        try:
            df = pd.read_sql_query(sql=sql_query, con=conn, params=query_params)
            return df
        finally:
            self.close_connection()

    def get_all_tables(self, database: Optional[str] = None, store_table_info: bool = False, print_tables_info: bool = False, as_dict: bool = False):
        """
        Fetch all tables from sys.tables. Optionally store/print TableInfo objects, or return raw rows/dicts.
        """
        sql_query = """
        SELECT * FROM sys.tables
        """
        self.open_connection(database)
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = None
        if store_table_info or print_tables_info:
            all_table_info = [TableInfo(*row) for row in rows]
            if print_tables_info:
                self.print_all_tables_info(all_table_info)
            if store_table_info:
                self.all_table_info = all_table_info
            result = all_table_info
        elif as_dict:
            result = [dict(zip(columns, row)) for row in rows]
        else:
            result = rows
        self.close_connection()
        return result

    def get_all_sql_columns(self, store_column_info=False, print_column_info=False, as_dict=False):
        sql_query = """
                    SELECT *
                    FROM sys.columns \
                    """
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = None
        if store_column_info or print_column_info:
            all_column_info = [TableInfo(*row) for row in rows]
            if print_column_info:
                self.print_all_tables_info(all_column_info)
            if store_column_info:
                self.all_column_info = all_column_info
            result = all_column_info
        elif as_dict:
            result = [dict(zip(columns, row)) for row in rows]
        else:
            result = rows
        self.conn.close()
        return result

    def get_all_sql_columns_for_table(self, table_name: str, store_column_info=False, print_column_info=False,
                                      as_dict=False):
        sql_query = f"""
        SELECT *
        FROM sys.columns
        WHERE object_id = OBJECT_ID('{table_name}')
        """
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = None
        if store_column_info or print_column_info:
            all_column_info = [TableInfo(*row) for row in rows]
            if print_column_info:
                self.print_all_tables_info(all_column_info)
            if store_column_info:
                self.all_column_info = all_column_info
            result = all_column_info
        elif as_dict:
            result = [dict(zip(columns, row)) for row in rows]
        else:
            result = rows
        self.conn.close()
        return result

    def get_all_references_for_column(self, column_name: str, store_column_info=False, print_column_info=False,
                                      as_dict=False):
        sql_get_referenced_entities = f"""
        SELECT *
        FROM sys.dm_sql_referenced_entities('{column_name}', 'OBJECT')
        """
        self.open_connection()
        cursor = self.conn.cursor()
        cursor.execute(sql_get_referenced_entities)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = None
        if store_column_info or print_column_info:
            all_column_info = [TableInfo(*row) for row in rows]
            if print_column_info:
                self.print_all_tables_info(all_column_info)
            if store_column_info:
                self.all_column_info = all_column_info
            result = all_column_info
        elif as_dict:
            result = [dict(zip(columns, row)) for row in rows]
        else:
            result = rows
        self.conn.close()
        return result

    @staticmethod
    def print_all_tables_info(all_tables_info: List['TableInfo']):
        print(f"Printing Tables Info")
        print(f"There are {len(all_tables_info)} tables.")
        for table in all_tables_info:
            print(table)

    @staticmethod
    def print_rows(rows: List):
        for idx, row in enumerate(rows):
            print(idx, ":", row)

    def execute_sql_file(self, file_path: str, database: Optional[str] = None):
        """
        Execute a SQL file, fetch all rows, commit, and return the result.
        """
        try:
            sql_query = self.read_sql_file(file_path)
            self.open_connection(database)
            cursor = self.conn.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            self.conn.commit()
            return rows
        except Exception as e:
            print(e)
            raise e
        finally:
            self.close_connection()

    def sql_file_to_df(self, file_path: str, database: Optional[str] = None) -> pd.DataFrame:
        """
        Reads a SQL file and loads the result into a DataFrame.
        """
        try:
            sql_query = self.read_sql_file(file_path)
            self.open_connection(database)
            df = pd.read_sql(sql_query, self.conn)
            return df
        except Exception as e:
            print(e)
            raise e
        finally:
            self.close_connection()

# Standalone utility function for parameter sanitization
def sanitize_params(params: dict) -> dict:
    if params is None:
        return {}
    sanitized_params = {k: html.escape(str(v)) for k, v in params.items()}
    return sanitized_params

def read_sql_lparams(file_path: str, database: str = None, query_params: List = None) -> pd.DataFrame:
    """
    Standalone function to read a SQL file and return a DataFrame, with error printing (from original utility_sql.py).
    """
    try:
        sql_query = TimsySqlUtil.read_sql_file(file_path)
        conn = TimsySqlUtil().open_connection(database)
        df = pd.read_sql_query(sql=sql_query, con=conn, params=query_params)
        return df
    except Exception as e:
        print("Failed to Read Sql File")
        print(e)
