import pandas as pd
import numpy as np
import os
from scipy import stats


# The function below processes one file

def process_file(file_path):
    # Load data
    df = pd.read_csv(file_path)

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
    all_dfs = []

    for file in os.listdir(data_folder):
        if file.endswith(".csv") and "clean" not in file:
            file_path = os.path.join(data_folder, file)

            df = process_file(file_path)
            all_dfs.append(df)

    final_df = pd.concat(all_dfs, ignore_index=True)
    return final_df


# Save cleaned data

def save_output(df, output_path):
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    data_folder = "data"
    output_file = "data/all_countries_clean.csv"

    final_df = process_all_files(data_folder)
    save_output(final_df, output_file)

    print("Processing complete. File saved to:", output_file)