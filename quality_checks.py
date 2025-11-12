import pandas as pd
import os

# --- DEFINE PATHS (The same as your previous run) ---
OUTPUT_DIRECTORY = r'E:\tech paiyan\output file'
OUTPUT_FILE_NAME = 'annual-enterprise-survey-2024-financial-year-provisional_CLEANED.csv'
CLEANED_FILE_PATH = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILE_NAME)

def check_cleaned_data(file_path: str):
    """
    Loads the cleaned CSV and performs essential checks to verify data quality.
    """
    print(f"--- 📊 Performing Data Checks on: {file_path} ---\n")
    
    try:
        # 1. Load the cleaned file
        df = pd.read_csv(file_path)
        
        # 2. Basic Inspection: Head and Shape
        print("## 1. Data Structure (Head & Shape)")
        print(f"Shape of the Cleaned Data (Rows, Columns): {df.shape}")
        print("\nFirst 5 Rows (df.head()):")
        print(df.head())
        print("-" * 50)
        
        # 3. Comprehensive Summary: Data Types and Non-Null Counts
        # This is the most important check for seeing if nulls were removed and types are correct.
        print("\n## 2. Column Information (df.info())")
        df.info()
        print("-" * 50)

        # 4. Statistical Summary: For Numerical Columns
        print("\n## 3. Statistical Summary (df.describe())")
        # Check central tendency, spread, and count to spot outliers/errors
        print(df.describe())
        print("-" * 50)
        
        # 5. Final Duplicates Check (Should be 0 if drop_duplicates was run correctly)
        duplicate_count = df.duplicated().sum()
        print(f"\n## 4. Final Duplicate Count Check")
        if duplicate_count == 0:
            print("✅ No duplicate rows found! Cleaning was successful.")
        else:
            print(f"⚠️ WARNING: {duplicate_count} duplicate rows still exist.")
        print("-" * 50)
        
        # 6. Check Missing Values (Should be 0 in the 'Non-Null Count' column in df.info())
        missing_values = df.isnull().sum().sum()
        print(f"\n## 5. Total Missing Values Check")
        if missing_values == 0:
             print("✅ No missing values found! Cleaning was successful.")
        else:
             print(f"⚠️ WARNING: {missing_values} total missing values still exist.")
        print("-" * 50)

        # 7. Check Value Counts for key columns (helps spot inconsistent categorical data)
        # Replace 'YOUR_KEY_COLUMN_NAME' with an actual column name from your data.
        # Example using the first column:
        first_column = df.columns[0]
        print(f"\n## 6. Value Counts for '{first_column}' (Top 10)")
        print(df[first_column].value_counts().head(10))
        print("-" * 50)

    except FileNotFoundError:
        print(f"❌ ERROR: Cleaned file not found at {file_path}. Please ensure the cleaning script ran successfully first.")
    except Exception as e:
        print(f"❌ An unexpected error occurred while checking the data: {e}")

# Call the function to check the data
if __name__ == "__main__":
    check_cleaned_data(CLEANED_FILE_PATH)
