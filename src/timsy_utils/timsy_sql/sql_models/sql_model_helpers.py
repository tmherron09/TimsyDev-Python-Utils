
def add_square_brackets(columns: list) -> list:
    if not columns:
        return columns
    return [f'[{column.strip()}]' if not (column.startswith('[') and column.endswith(']'))
            else column for column in columns]


def add_square_bracket(item: str | None) -> str:
    if not item:
        return item
    item = item.strip()
    return item if not (item.startswith('[') and item.endswith(']')) else f'[{item}]'


def format_from(schema: str, table: str, alias: str = None) -> str:
    if alias:
        return f'FROM {schema}.{table} AS {alias}'
    return f'FROM {schema}.{table}'


def format_join(join_type: str, source_table: dict, target_table: dict, on_source: dict, on_target: dict) -> str:
    source = format_from(source_table['schema'], source_table.get('table', 'dbo'), source_table.get('alias', None))
    target = format_from(target_table['schema'], target_table.get('table', 'dbo'), target_table.get('alias', None))
    on_source = add_square_bracket(on_source['column']) if on_source else None
    on_target = add_square_bracket(on_target['column']) if on_target else None
    return f'{join_type} {source} JOIN {target} ON {on_source} = {on_target}'


def format_columns(sql: str, columns: list) -> str:
    columns_str = '\n\t,'.join(columns)
    return sql.format(columns=columns_str)
