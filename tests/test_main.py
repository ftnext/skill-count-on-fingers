import filecmp
from pathlib import Path

from countup.__main__ import main


def test_csvファイルをcountupできる(tmp_path):
    tests_dir = Path(__file__).parent
    csv_case_dir = tests_dir / "resources" / "csv"

    main(csv_case_dir / "example.csv", tmp_path)

    assert filecmp.cmp(
        csv_case_dir / "expected" / "column1.csv",
        tmp_path / "example" / "column1.csv",
    )
    assert filecmp.cmp(
        csv_case_dir / "expected" / "column2.csv",
        tmp_path / "example" / "column2.csv",
    )
