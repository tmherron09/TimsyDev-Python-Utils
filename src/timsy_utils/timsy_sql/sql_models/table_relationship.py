

class TableRelationship:
    def __init__(self, database_a: str | None, database_b: str | None, schema_a: str = 'dbo', schema_b: str = 'dbo', *,
                 table_a: str, table_b: str, column_a: str, column_b: str, alias_a: str = None, alias_b: str = None):
        self.table_a = {"database": database_a, "schema": schema_a, "table": table_a, "column": column_a,
                        "alias": alias_a}
        self.table_b = {"database": database_b, "schema": schema_b, "table": table_b, "column": column_b,
                        "alias": alias_b}

    @classmethod
    def from_dict(cls, table_a: dict, table_b: dict):
        return cls(table_a.get('database', None), table_b.get('database', None), table_a.get('schema', 'dbo'),
                   table_b.get('schema', 'dbo'), table_a=table_a['table'], table_b=table_b['table'],
                   column_a=table_a['column'], column_b=table_b['column'], alias_a=table_a.get('alias', None),
                   alias_b=table_b.get('alias', None))

