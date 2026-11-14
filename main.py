import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "dirty_cafe_sales.csv"

COLUMNS = {
    "Transaction ID": "transcation_id",
    "Item": "item",
    "Quantity": "quantity",
    "Price Per Unit": "price_per_unit",
    "Total Spent": "total_spent",
    "Payment Method": "payment_method",
    "Location": "location",
    "Transaction Date": "transaction_date",
}

# df = raw.rename(columns=column_names)


def prepare_sales(raw: pd.DataFrame):
    df = raw[list(COLUMNS)].rename(columns=COLUMNS)
    # print(df)


def clean_sales():
    raw = pd.read_csv(INPUT_FILE, dtype="string", keep_default_na=False)
    print(raw)
    prepare_sales(raw)


# def main():
#     pass

# clean_sales()
# main()
