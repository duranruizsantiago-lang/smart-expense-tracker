from __future__ import annotations
import csv
import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from .categories import CATEGORY_KEYWORDS, DEFAULT_CATEGORY
from .utils import parse_month, to_float


@dataclass
class Transaction:
    date: datetime
    description: str
    amount: float
    category: str


def categorize(description: str, amount: float) -> str:
    desc = description.lower()
    if amount > 0:
        return "Income"
    for category, keywords in CATEGORY_KEYWORDS.items():
        if category == "Income":
            continue
        if any(k in desc for k in keywords):
            return category
    return DEFAULT_CATEGORY


def load_csv(path: Path) -> list[Transaction]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    txs: list[Transaction] = []
    with path.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = datetime.strptime(row["date"], "%Y-%m-%d")
            description = row["description"].strip()
            amount = to_float(row["amount"])
            category = categorize(description, amount)
            txs.append(Transaction(date, description, amount, category))
    return txs


def filter_month(txs: list[Transaction], year: int, month: int) -> list[Transaction]:
    return [t for t in txs if t.date.year == year and t.date.month == month]


def summarize(txs: list[Transaction]) -> dict:
    total = sum(t.amount for t in txs)
    by_cat: dict[str, float] = {}
    for t in txs:
        by_cat[t.category] = by_cat.get(t.category, 0.0) + t.amount
    return {"total": total, "by_category": dict(sorted(by_cat.items(), key=lambda x: x[0]))}


def export_report(txs: list[Transaction], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "description", "amount", "category"])
        for t in txs:
            writer.writerow([t.date.strftime("%Y-%m-%d"), t.description, f"{t.amount:.2f}", t.category])


def main() -> None:
    parser = argparse.ArgumentParser(description="Smart Expense Tracker (CLI)")
    parser.add_argument("--input", required=True, help="Path to CSV file")
    parser.add_argument("--month", required=True, help="Month filter in YYYY-MM")
    parser.add_argument("--export", default=None, help="Export filtered transactions to CSV")

    args = parser.parse_args()
    year, month = parse_month(args.month)
    txs = load_csv(Path(args.input))
    txs_month = filter_month(txs, year, month)

    summary = summarize(txs_month)
    print(f"\nðŸ“… Summary for {year}-{month:02d}")
    print(f"Total: {summary['total']:.2f}")
    print("\nBy category:")
    for cat, value in summary["by_category"].items():
        print(f" - {cat}: {value:.2f}")

    if args.export:
        export_report(txs_month, Path(args.export))
        print(f"\nâœ… Exported report to: {args.export}")


if __name__ == "__main__":
    main()
