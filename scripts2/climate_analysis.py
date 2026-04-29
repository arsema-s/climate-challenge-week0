import pandas as pd
import numpy as np
import os
from scipy import stats

import argparse

import logging
logging.basicConfig(level=logging.INFO)


# The function below processes one file

def process_file(file_path):
    # Load data
    logging.info(f"Loading file: {file_path}")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except Exception as e:
        logging.error(f"Error loading file {file_path}: {e}")
        return None

    # Extract country dynamically
    country = os.path.basename(file_path).replace(".csv", "")
    df["Country"] = country

    # Create date column
    df["date"] = pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")

    # Extract month
    df["Month"] = df["date"].dt.month

    # Replace -999
    df.replace(-999, np.nan, inplace=True)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.ffill()

    # Outlier removal
    cols = ["T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR", "RH2M", "WS2M", "WS2M_MAX"]
    z_scores = np.abs(stats.zscore(df[cols], nan_policy='omit'))
    df = df[(z_scores < 3).all(axis=1)]

    return df


# The function below processes all files

def process_all_files(data_folder):
    import os
    import pandas as pd

    all_dfs = []

    for file in os.listdir(data_folder):
        if not file.endswith(".csv"):
            continue

        file_path = os.path.join(data_folder, file)

        try:
            df = pd.read_csv(file_path)

            required_cols = ["YEAR", "DOY", "T2M"]
            if not all(col in df.columns for col in required_cols):
                print(f"Skipping {file} — missing required columns")
                continue

            df["Country"] = file.replace(".csv", "")
            all_dfs.append(df)

        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue

    if not all_dfs:
        raise ValueError("No valid data files were processed.")

    final_df = pd.concat(all_dfs, ignore_index=True)
    return final_df


# Save cleaned data

def save_output(df, output_path):
    df.to_csv(output_path, index=False)


# if __name__ == "__main__":
#     data_folder = "data"
#     output_file = "data/all_countries_clean.csv"

#     final_df = process_all_files(data_folder)
#     save_output(final_df, output_file)

#     print("Processing complete. File saved to:", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Climate data processing script")

    # parser.add_argument("input_folder", help="Path to folder containing CSV files")
    # parser.add_argument("output_file", help="Path to save cleaned dataset")
    parser.add_argument("--input", default="data", help="Input folder")
    parser.add_argument("--output", default="data/output.csv", help="Output file")


    args = parser.parse_args()

    # data_folder = args.input_folder
    # output_file = args.output_file
    data_folder = args.input
    output_file = args.output

    try:
        final_df = process_all_files(data_folder)

        if final_df is not None:
            save_output(final_df, output_file)
            logging.info(f"Processing complete. File saved to: {output_file}")
        else:
            logging.error("Processing failed. No output generated.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    logging.info(f"Processing complete. File saved to: {output_file}")