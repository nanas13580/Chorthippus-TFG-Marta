import pandas as pd
from Bio import SeqIO
import re

# === 1. Define the data folder path ===
folder_path = '/home/anaisthibert/Chorthippus-TFG-Marta/data_chortippus/'

# === 2. Load required files ===
clines_df = pd.read_excel(f'{folder_path}clines_data_clean.xlsx')
positions_df = pd.read_csv(f'{folder_path}grasshopperRef.positions', sep='\t', header=None)
snp_names = pd.read_csv(f'{folder_path}snp_names', sep='\t', header=None)

# Columns you want to ask the user for
interactive_columns = ['Portalet_slope', 'PaysBasco_slope']

# Default values for the other columns
filter_values = {}

# Ask only for the slope columns
for col in interactive_columns:
    val = input(f"Which value to keep for '{col}'? (VERDADERO/FALSO): ").strip().upper()
    while val not in ['VERDADERO', 'FALSO']:
        val = input(f"Invalid input. Choose VERDADERO or FALSO for '{col}': ").strip().upper()
    # This line must be INSIDE the loop!
    filter_values[col] = True if val == "VERDADERO" else False

# === 5. Apply filters to the dataframe ===
filtered_df = clines_df.copy()
for col, val in filter_values.items():
    filtered_df = filtered_df[filtered_df[col] == val]

print("✅ Step 1 - After filtering by VERDADERO/FALSO:")
print(filtered_df.head())
print(f"→ Total SNPs matched: {len(filtered_df)}\n")

# === 6. Extract numeric SNP ID from locus format like 'chr1_32418580.Portalet' → 32418580 ===
filtered_df['snp_ID'] = filtered_df.iloc[:, 0].apply(
    lambda x: int(re.search(r'_(\d+)\.', str(x)).group(1)) if re.search(r'_(\d+)\.', str(x)) else None
)
print("✅ Step 2 - Extracted numeric SNP IDs:")
print(filtered_df['snp_ID'].dropna().head())
print(f"→ Total extracted SNP IDs: {filtered_df['snp_ID'].notna().sum()}\n")

# === 7. Create a dataframe for selected SNPs ===
snp_df = pd.DataFrame(filtered_df['snp_ID'].dropna().astype(int), columns=['snp_ID'])
snp_df['range'] = None
snp_df['cluster'] = None
print("✅ Step 3 - snp_df initialized:")
print(snp_df.head())
print(f"→ Total SNPs in snp_df: {len(snp_df)}\n")

# === 8. Match each SNP to its range and cluster using the positions file ===
print(f"🧪 Type of snp_ID: {snp_df['snp_ID'].dtype}")
for index, row in snp_df.iterrows():
    snp_id = row['snp_ID']
    for _, pos_row in positions_df.iterrows():
        cluster_full = pos_row[0]  # e.g., "catalog_normal_noMito.fasta:cluster_6"
        pos_str = pos_row[1]       # e.g., "chr1:1-9898"
        pos_interval = pos_str.split(':')[1]
        pos_start, pos_end = map(int, pos_interval.split('-'))
        if pos_start <= snp_id <= pos_end:
            snp_df.at[index, 'range'] = pos_str
            snp_df.at[index, 'cluster'] = cluster_full.split(':')[-1]
            break
# Step 4.5 - Show unmatched SNPs
unmatched_snps = snp_df[snp_df['cluster'].isna()]
print(f"\n❌ SNPs that were NOT matched to any cluster: {len(unmatched_snps)}")
print(unmatched_snps['snp_ID'].tolist())

print("✅ Step 4 - snp_df after matching SNPs to positions:")
print(snp_df[['snp_ID', 'range', 'cluster']].head())
print(f"→ SNPs matched to clusters: {snp_df['cluster'].notna().sum()}\n")

# === 9. Load the cluster sequences from the FASTA file ===
fasta_file = f'{folder_path}clusters.fasta'
cluster_sequences = {}
for record in SeqIO.parse(fasta_file, "fasta"):
    cluster_sequences[record.id] = str(record.seq)

# === 10. Add corresponding sequence to each SNP based on its cluster ===
snp_df['sequence'] = snp_df['cluster'].apply(lambda x: cluster_sequences.get(x, None))
print("✅ Step 5 - Final snp_df with sequences:")
print(snp_df[['snp_ID', 'cluster', 'sequence']].head())
print(f"→ SNPs with sequence found: {snp_df['sequence'].notna().sum()}\n")

# === 11. Display the final dataframe ===
print(snp_df)

# Optional: save to file
snp_df.to_csv(f'{folder_path}snp_sequences_filtered.csv', index=False)
