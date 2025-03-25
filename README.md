# Chorthippus-TFG-Marta

## Required Files

Before cloning the repository, make sure you have the following files in a folder named `data_chortippus` inside `~/Chorthippus-TFG-Marta/`:

- **Base datos genes** (Excel file)
- **gc_onerow_per_locus_transects_separated_DB** (Excel file)
- **catalog_normal_annotated.fasta** (FASTA file)
- **grasshopperRef.positions** (Positions file)
- **snp_names** (CSV file)

### Folder Structure:

The folder `data_chortippus` should be placed **inside** the project folder `Chorthippus-TFG-Marta`, which should be located in your home directory (`~/`). The full folder structure will look like this. The full folder structure will look like this **before cloning the repository**:

```
~/Chorthippus-TFG-Marta/  
    └── data_chortippus/  
        ├── Base datos genes.xlsx  
        ├── gc_onerow_per_locus_transects_separated_DB.xlsx  
        ├── catalog_normal_annotated.fasta  
        ├── grasshopperRef.positions  
        └── snp_names.csv
```

Once you clone the repository, your folder structure will be updated to look like this:

```
~/Chorthippus-TFG-Marta/  
    ├── data_chortippus/        # Keep this folder as is (the data files)  
    ├── analyse_snp.py          # Python script for analysis  
    └── README.md               # This README file
```

**Important:** Do not delete or move the `data_chortippus` folder! It must stay in `~/Chorthippus-TFG-Marta/` for the script to function correctly.

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone <repository_url> ~/Chorthippus-TFG-Marta/
   ```

2. Navigate to the project folder:

  ```bash
  cd ~/Chorthippus-TFG-Marta/
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
   
6. You can now run the script using Python:

 ```bash
  python analyse_snp.py
  ```
