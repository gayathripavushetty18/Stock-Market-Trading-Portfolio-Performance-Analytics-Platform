import pandas as pd
import glob
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

RAW_PATH = "data/raw/stocks/"
PROCESSED_PATH = "data/processed/"

Path(PROCESSED_PATH).mkdir(parents=True, exist_ok=True)

EXPECTED_COLUMNS = {
    "date", "open", "high", "low", "close", "volume", "company", "sector"
}

def ingest_and_validate():
    files = glob.glob(f"{RAW_PATH}/*.csv")
    all_data = []

    if not files:
        logging.error("No stock files found for ingestion")
        return

    for file in files:
        try:
            df = pd.read_csv(file)

            # Standardize column names
            df.columns = [c.lower() for c in df.columns]

            # Schema validation
            if not EXPECTED_COLUMNS.issubset(df.columns):
                raise ValueError(f"Schema mismatch in file: {file}")

            # Type validation
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
            numeric_cols = ["open", "high", "low", "close", "volume"]
            df[numeric_cols] = df[numeric_cols].apply(
                pd.to_numeric, errors="coerce"
            )

            # Drop invalid rows
            initial_count = len(df)
            df.dropna(inplace=True)
            final_count = len(df)

            logging.info(
                f"{file} | rows before: {initial_count}, after cleaning: {final_count}"
            )

            all_data.append(df)

        except Exception as e:
            logging.error(f"Failed processing {file} | {e}")

    final_df = pd.concat(all_data, ignore_index=True)

    output_file = f"{PROCESSED_PATH}/clean_stock_data.csv"
    final_df.to_csv(output_file, index=False)

    logging.info(f"✅ Ingestion completed. Output saved to {output_file}")

if __name__ == "__main__":
    ingest_and_validate()
