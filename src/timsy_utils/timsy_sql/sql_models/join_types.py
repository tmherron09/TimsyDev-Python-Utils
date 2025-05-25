from enum import Enum


class JoinType(Enum):
    INNER_JOIN = "INNER JOIN"
    LEFT_JOIN = "LEFT JOIN"
    RIGHT_JOIN = "RIGHT JOIN"
    FULL_OUTER_JOIN = "FULL OUTER JOIN"