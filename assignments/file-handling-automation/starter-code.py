import csv
from pathlib import Path


def load_csv_data(filepath):
    """Load CSV rows from the given file path and return a list of dictionaries."""
    data = []
    with open(filepath, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def summarize_sales(data):
    """Return a text summary of total quantity and sales value from the CSV data."""
    total_quantity = 0
    total_value = 0.0

    for row in data:
        quantity = int(row["quantity"])
        price = float(row["price"])
        total_quantity += quantity
        total_value += quantity * price

    return (
        f"Sales Summary\n"
        f"Total items sold: {total_quantity}\n"
        f"Total sales value: ${total_value:.2f}\n"
    )


def save_summary(summary, output_file):
    """Write the summary text to the output file path."""
    output_path = Path(output_file)
    output_path.write_text(summary, encoding="utf-8")
    return output_path


def run_report():
    """Load data, generate a sales summary, and save it to a report file."""
    data_file = Path(__file__).parent / "sample-data.csv"
    report_file = Path(__file__).parent / "sales-report.txt"

    data = load_csv_data(data_file)
    summary = summarize_sales(data)
    saved_path = save_summary(summary, report_file)

    print(f"Report saved to: {saved_path}")


if __name__ == "__main__":
    run_report()
