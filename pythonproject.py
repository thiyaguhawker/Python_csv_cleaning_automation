import pandas as pd
import os

def clean_duplicates_and_save(input_path: str, output_path: str):
    """
    Reads a CSV, removes duplicate rows, and saves the cleaned DataFrame 
    to the specified output path.
    """
    try:
        # 1. Read the CSV file
        print(f"Reading CSV from: {input_path}")
        df = pd.read_csv(input_path)
        
        print(f"Initial number of records: {len(df)}")
        
        # 2. Identify and Remove Duplicates
        df_cleaned = df.drop_duplicates()
        
        print(f"Number of records after removing duplicates: {len(df_cleaned)}")
        
        # 3. Ensure the output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            print(f"Creating output directory: {output_dir}")
            # The 'exist_ok=True' flag prevents an error if the directory already exists
            os.makedirs(output_dir, exist_ok=True)
            
        # 4. Save the cleaned DataFrame
        df_cleaned.to_csv(output_path, index=False)
        
        print("\n✨ Cleaning complete!")
        print(f"Cleaned data saved successfully to: {output_path}")

    except FileNotFoundError:
        print(f"❌ ERROR: Input file not found at {input_path}. Please check the path and file name.")
    except Exception as e:
        print(f"❌ An error occurred during processing: {e}")

# --- SET YOUR UPDATED PATHS HERE ---

# Path A (Input Path) - The location of your raw file
INPUT_FILE_PATH = r'E:\tech paiyan\raw data\annual-enterprise-survey-2024-financial-year-provisional.csv'

# Path B (Output Path) - The directory you requested, with a file name appended
# The `os.path.join` function is used here for robust path construction.
OUTPUT_DIRECTORY = r'E:\tech paiyan\output file'
OUTPUT_FILE_NAME = 'annual-enterprise-survey-2024-financial-year-provisional_CLEANED.csv'
OUTPUT_FILE_PATH = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILE_NAME)

# Call the function
if __name__ == "__main__":
    clean_duplicates_and_save(INPUT_FILE_PATH, OUTPUT_FILE_PATH)
