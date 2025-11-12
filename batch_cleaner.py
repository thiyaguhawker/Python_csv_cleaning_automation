import pandas as pd
import os
import shutil

# --- DEFINE PATHS ---
INPUT_DIR = r'E:\tech paiyan\raw data'
OUTPUT_DIR = r'E:\tech paiyan\output file'
PROCESSED_DIR = os.path.join(INPUT_DIR, 'processed') # Directory to move originals after cleaning

def clean_and_move_file(input_filepath: str, output_filepath: str):
    """Performs the cleaning logic on a single file."""
    try:
        df = pd.read_csv(input_filepath)
        
        # --- Cleaning Logic (as defined before) ---
        initial_count = len(df)
        df_cleaned = df.dropna()            # Remove rows with missing values
        df_cleaned = df_cleaned.drop_duplicates() # Remove duplicate rows
        final_count = len(df_cleaned)
        
        # Save the cleaned file
        df_cleaned.to_csv(output_filepath, index=False)
        
        print(f"  ✅ Cleaned: {os.path.basename(input_filepath)}")
        print(f"     - Records: {initial_count} -> {final_count} (Lost {initial_count - final_count})")
        
        return True
    except Exception as e:
        print(f"  ❌ FAILED to process {os.path.basename(input_filepath)}: {e}")
        return False

def run_batch_cleaning():
    """Iterates through all CSV files in the input directory, cleans them, and moves the originals."""
    print(f"--- 🧹 Starting Batch Cleaning at {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
    
    # Ensure directories exist
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    
    files_to_process = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith('.csv')]
    
    if not files_to_process:
        print("➡️ No new CSV files found to process.")
        return

    print(f"Found {len(files_to_process)} file(s) to process.")

    for filename in files_to_process:
        input_filepath = os.path.join(INPUT_DIR, filename)
        
        # Create the cleaned filename (e.g., adds _CLEANED)
        base, ext = os.path.splitext(filename)
        output_filename = f"{base}_CLEANED{ext}"
        output_filepath = os.path.join(OUTPUT_DIR, output_filename)
        
        if clean_and_move_file(input_filepath, output_filepath):
            # Move the original file to the processed folder
            processed_filepath = os.path.join(PROCESSED_DIR, filename)
            shutil.move(input_filepath, processed_filepath)
            print(f"  ➡️ Moved original to: {PROCESSED_DIR}")

    print("--- ✅ Batch Cleaning Complete ---")

if __name__ == "__main__":
    run_batch_cleaning()
