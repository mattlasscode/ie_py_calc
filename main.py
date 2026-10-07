"""Command-line interface for the simple calculator."""

import argparse
import sys
from typing import List, Optional

from calculator import (
    add,
    compound_growth,
    divide,
    multiply,
    percentage_change,
    subtract,
)


OPERATIONS = {
    "add": (add, 2),
    "subtract": (subtract, 2),
    "multiply": (multiply, 2),
    "divide": (divide, 2),
    "percentage_change": (percentage_change, 2),
    "compound_growth": (compound_growth, 3),
}


def run_operation(operation: str, operands: List[float]) -> float:
    """Execute a named operation with the provided operands."""
    if operation not in OPERATIONS:
        raise ValueError(f"Unknown operation: {operation}")

    func, expected_count = OPERATIONS[operation]
    if len(operands) != expected_count:
        raise ValueError(
            f"'{operation}' requires {expected_count} operands, got {len(operands)}"
        )

    return func(*operands)


def main(argv: Optional[List[str]] = None) -> int:
    """Parse arguments, run the requested calculation, and print the result."""
    parser = argparse.ArgumentParser(
        description="Simple calculator supporting basic financial and arithmetic operations."
    )
    parser.add_argument(
        "operation",
        choices=list(OPERATIONS.keys()),
        help="Operation to perform",
    )
    parser.add_argument(
        "operands",
        type=float,
        nargs="+",
        help="Numeric operands for the operation",
    )

    args = parser.parse_args(argv)

    try:
        result = run_operation(args.operation, args.operands)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
