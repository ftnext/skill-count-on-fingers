from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class Countup:
    column: str
    counter: Counter

    def most_common(self):
        return self.counter.most_common()


def count_columns(rows: Sequence[dict[str, str]]) -> list[Countup]:
    columns = rows[0].keys()
    return [
        Countup(column, Counter(row[column] for row in rows))
        for column in columns
    ]
