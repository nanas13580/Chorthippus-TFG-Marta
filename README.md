# Chorthippus-TFG-Marta

Make sure you have the required files in a folder named data_chortippus located on your desktop. The folder should contain the following files:

Base datos genes (Excel file)

gc_onerow_per_locus_transects_separated_DB (Excel file)

catalog_normal_annotated.fasta (FASTA file)

grasshopperRef.positions (Positions file)

snp_names (CSV file)

The script assumes that the folder data_chortippus is placed directly on your desktop. If you decide to use a different location, make sure to update the file paths in the script accordingly.

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project folder:

  ```bash
  cd <repository_folder>
  ```

3. Create a virtual environment:

  ```bash
  python3 -m venv venv
  ```

4. Activate the virtual environment:

  ```bash
  source venv/bin/activate
  ```
5. Download the packages

   ```bash
   pip install pandas biopython
   ```
Note: The data_chortippus folder is included in the .gitignore file, so it is not tracked by Git. You must add the necessary files manually.

6. You can now run the script using Python:

 ```bash
  python analyse_snp.py
  ```

## Notes

This project requires a Python environment with the following libraries: pandas, biopython, etc.
