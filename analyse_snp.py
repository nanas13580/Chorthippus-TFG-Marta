import os
import pandas as pd
from Bio import SeqIO

# Define folder path relative to the script
folder_path = os.path.join(os.getcwd(), 'data_chortippus')  # This uses the current working directory

# Load the Excel and CSV files
base_datos_genes = pd.read_excel(f'{folder_path}/Base datos genes.xlsx')
gc_locus = pd.read_excel(f'{folder_path}/gc_onerow_per_locus_transects_separated_DB.xlsx')
positions_df = pd.read_csv(f'{folder_path}/grasshopperRef.positions', sep='\t')  # Assuming tab-separated
snp_names = pd.read_csv(f'{folder_path}/snp_names.txt', sep='\t')  # Adjust separator if necessary

# Print the first few rows of each DataFrame
print(base_datos_genes.head())
print(gc_locus.head())
print(positions_df.head())
print(snp_names.head())
