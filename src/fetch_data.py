"""
fetch_data.py

Fetches the Diabetes 130-US Hospitals dataset (ID 296) from UCI Machine Learning Repository
and saves it as a CSV for reproducible RWE analysis.
"""

from ucimlrepo import fetch_ucirepo
import pandas as pd
from pathlib import Path
import sys

def fetch_and_save():
    print("Fetching Diabetes 130-US Hospitals dataset (ID=296)...")
    try:
        # 1) Fetch desde UCI (id=296)
        ds = fetch_ucirepo(id=296)
        
        # 2) Features y target
        X = ds.data.features
        y = ds.data.targets
        
        # 3) Unir en un solo dataframe
        print("Concatenating features and targets...")
        df = pd.concat([X, y], axis=1)
        
        # 4) Guardar local
        output_dir = Path("data/raw")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / "diabetes_uci296.csv"
        
        df.to_csv(output_file, index=False)
        print(f"✅ Success! Data saved to {output_file}")
        print(f"Shape: {df.shape}")
        
        # Opcional: metadata dump
        print("\n--- Metadata ---")
        print(ds.metadata.abstract if ds.metadata.abstract else "No abstract")
        
        return df
        
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        sys.exit(1)

def verify(df):
    print("\n--- Verification ---")
    print(df.columns[:10])
    print("\nMissing values (top 10):")
    print(df.isna().mean().sort_values(ascending=False).head(10))

if __name__ == "__main__":
    df = fetch_and_save()
    if df is not None:
        verify(df)
