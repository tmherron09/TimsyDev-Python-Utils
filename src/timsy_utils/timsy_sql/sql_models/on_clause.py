

class on_clause:
    def __init__(self, schema: str | None, table: str, column: str, columns: List = None, alias: str = None):
        self.schema = schema if schema else 'dbo'
        self.table = table
        self.column = add_square_bracket(column)
        self.columns = add_square_brackets(columns)
        self.alias = add_square_bracket(alias)
        self.has_on_join_multiple_columns = len(self.columns) > 1

    def join_to(self) -> str:
        if self.alias:
            return f'{self.schema}.{self.table} AS {self.alias}'
        return f'{self.schema}.{self.table}'

    @classmethod
    def from_dict(cls, table: dict):
        return cls(table.get('schema', 'dbo'), table['table'], table['column'], table.get('alias', None))

