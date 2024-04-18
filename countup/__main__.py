import argparse
import csv
from pathlib import Path

from countup.core import count_columns


def read_csv(file: Path):
    with open(file, encoding="utf8") as fin:
        reader = csv.DictReader(fin)
        rows = list(reader)
    return rows


def read_jsonl(file: Path):
    import jsonlines

    with jsonlines.open(file) as reader:
        rows = list(reader)
    return rows


reader_functions = {"csv": read_csv, "jsonl": read_jsonl}


def main(file: Path, output_root: Path):
    suffix = file.suffix.lstrip(".")
    reader_func = reader_functions[suffix]
    rows = reader_func(file)

    counters = count_columns(rows)

    output_dir_path = output_root / file.stem
    output_dir_path.mkdir(parents=True, exist_ok=True)
    for counter in counters:
        with open(output_dir_path / f"{counter.column}.csv", "w") as fout:
            writer = csv.writer(fout)
            writer.writerows(counter.most_common())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()

    main(args.file, args.output_root)
