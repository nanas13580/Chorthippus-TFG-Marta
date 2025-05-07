# 🦗 Chorthippus-TFG-Marta

## Required Files (Not Included)

⚠️ This repository **does not include the required data files**
Before cloning the repository, make sure you have the following files in a folder named `data_chorthippus` inside `~/Chorthippus-TFG-Marta/` :

- **clines_data_clean.xlsx** (Excel file)
- **clusters.fasta** (Fasta file)
- **grasshopperRef.positions** (Positions file)
- **snp_names** (list of SNP IDs)

### Folder Structure :

The folder `data_chortippus` should be placed **inside** the project folder `Chorthippus-TFG-Marta`, which should be located in your home directory (`~/`). The full folder structure will look like this. The full folder structure will look like this **before cloning the repository** :

```
~/Chorthippus-TFG-Marta/  
    └── data_chorthippus/  
        ├── clines_data_clean.xlsx  
        ├── clusters.fasta  
        ├── grasshopperRef.positions  
        └── snp_names
```

Once you clone the repository, your folder structure will be updated to look like this :

```
~/Chorthippus-TFG-Marta/  
    ├── data_chorthippus/       # Keep this folder as is (the data files)  
    ├── analyse_snp.py          # Python script for analysis
    ├── .gitignore              # Ignore this file  
    └── README.md               # This README file
```

**Important :** Do not delete or move the `data_chorthippus` folder! It must stay in `~/Chorthippus-TFG-Marta/` for the script to function correctly.

## Installation and Usage

1. Clone the repository :

  ```bash
  git clone https://github.com/nanas13580/Chorthippus-TFG-Marta ~/Chorthippus-TFG-Marta/
  ```

2. Navigate to the project folder :

  ```bash
  cd ~/Chorthippus-TFG-Marta/
  ```

3. Create a virtual environment :

  ```bash
  python3 -m venv venv
  ```

4. Activate the virtual environment :

  ```bash
  source venv/bin/activate
  ```

5. Download the packages :

 ```bash
   pip install pandas biopython
 ```
   
6. You can now run the script using Python :

 ```bash
  python analyse_snp.py
 ```
7. When finished, you can deactivate the virtual environment :

 ```bash
  deactivate
 ```
## Output

After running the script, the following file will be created :

  ```bash
 ~/Chorthippus-TFG-Marta/data_chorthippus/snp_sequences_filtered.csv
  ```

It contains the filtered SNPs, their cluster ID, range, and nucleotide sequence.


