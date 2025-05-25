


class JoinTable:
    def __init__(self, join_type: JoinType, on_source: on_clause,
                 on_target: on_clause):
        self.join_type = join_type
        self.on_source = on_source
        self.on_target = on_target

    @classmethod
    def from_direct(cls, join_type: JoinType, source_schema: str | None, source_table: str, source_column: str,
                    target_schema: str | None, target_table: str, target_column: str, source_alias: str = None,
                    target_alias: str = None):
        on_source = on_clause(source_schema, source_table, source_column, source_alias)
        on_target = on_clause(target_schema, target_table, target_column, target_alias)
        return cls(join_type, on_source, on_target)

    @classmethod
    def from_table_relationship(cls, join_type: JoinType, table_relationship: TableRelationship):
        return cls(join_type, on_clause.from_dict(table_relationship.table_a), on_clause.from_dict(table_relationship.table_b))

    def format_from(self, schema: str, table: str, alias: str = None) -> str:
        if alias:
            return f'FROM {schema}.{table} AS {alias}'
        return f'FROM {schema}.{table}'

    def format_join(self) -> str:
        return f'\n\t{self.join_type} {self.on_target.join_to()}\n\t\tON {self.on_source.column} = {self.on_target.column}'
