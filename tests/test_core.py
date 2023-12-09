from countup.core import Countup, count_columns


def test_カラムごとにカウントできる():
    rows = [
        {"column1": "aaa", "column2": "ham"},
        {"column1": "bbb", "column2": "spam"},
        {"column1": "ccc", "column2": "ham"},
    ]

    actual = count_columns(rows)

    expected = [
        Countup("column1", {"aaa": 1, "bbb": 1, "ccc": 1}),
        Countup("column2", {"ham": 2, "spam": 1}),
    ]
    assert actual == expected
