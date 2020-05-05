"""pyutils.py: utility functions."""
import csv
import random
import string
from collections import defaultdict
from typing import Dict, List, Sequence


def argmin(sequence: Sequence) -> int:
    """Find the argmin of a sequence."""
    return min(range(len(sequence)), key=lambda i: sequence[i])


def argmax(sequence: Sequence) -> int:
    """Find the argmax of a sequence."""
    return max(range(len(sequence)), key=lambda i: sequence[i])


def rand_str(length: int, alphabet: int = string.ascii_letters + string.digits) -> str:
    """Return a random string of specifiend `length` from `alphabet`."""
    return "".join((random.choice(alphabet) for _ in range(length)))


def csv_read_columns(csvfile: str) -> Dict[str, List[str]]:
    """Read a csv file into a dictionary mapping column headers to lists."""
    table = defaultdict(list)
    with open(csvfile, "r", newline="") as f:
        reader = csv.reader(f)
        keys = next(reader)
        for row in reader:
            for key, item in zip(keys, row):
                table[key].append(item)
    return dict(table)
