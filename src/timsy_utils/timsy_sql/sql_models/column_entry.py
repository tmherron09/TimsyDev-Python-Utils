

@dataclass
class ColumnEntry:
    name: str
    sql_column_type: SQLColumnType
    column_instance: List[ColumnInstance]
    procs_using: List[Proc]

