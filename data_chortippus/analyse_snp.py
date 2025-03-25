import pandas as pd
from Bio import SeqIO

# Define the folder path
folder_path = '/home/anaisthibert/Chorthippus-TFG-Marta/data_chortippus/'

# Load the files with full paths
base_datos_genes = pd.read_excel(f'{folder_path}Base datos genes.xlsx')
gc_locus = pd.read_excel(f'{folder_path}gc_onerow_per_locus_transects_separated_DB.xlsx')
positions_df = pd.read_csv(f'{folder_path}grasshopperRef.positions', sep='\t', header=None)  # Tab-separated file
snp_names = pd.read_csv(f'{folder_path}snp_names', sep='\t', header=None)  # No header in this file

# Extract the first column of snp_names into a DataFrame
snp_df = pd.DataFrame(snp_names.iloc[:, 0].values, columns=['snp_ID'])

# Create 'range' and 'cluster' columns
snp_df['range'] = None
snp_df['cluster'] = None

# For testing, select only the first 20 SNPs
test_snp_df = snp_df.head(20).copy()

# For each SNP in test_snp_df, find the corresponding range in positions_df
for index, row in test_snp_df.iterrows():
    snp_id = row['snp_ID']
    for _, pos_row in positions_df.iterrows():
        # pos_row[0]: full cluster name, e.g., "catalog_normal_noMito.fasta:cluster_6"
        # pos_row[1]: range, e.g., "chr1:1-9898"
        cluster_full = pos_row[0]
        pos_str = pos_row[1]
        # Extract the interval after the ":" (e.g., "1-9898")
        pos_interval = pos_str.split(':')[1]
        pos_start, pos_end = map(int, pos_interval.split('-'))
        # If the SNP is within this interval, assign the range and cluster
        if pos_start <= snp_id <= pos_end:
            test_snp_df.loc[index, 'range'] = pos_str
            test_snp_df.loc[index, 'cluster'] = cluster_full.split(':')[-1]
            break

# Load the FASTA file containing cluster sequences
fasta_file = f'{folder_path}catalog_normal_annotated.fasta'
cluster_sequences = {}
for record in SeqIO.parse(fasta_file, "fasta"):
    cluster_sequences[record.id] = str(record.seq)

# Add the 'sequence' column by mapping the cluster to sequences, or None if not found
test_snp_df['sequence'] = test_snp_df['cluster'].apply(lambda x: cluster_sequences.get(x, None))

# Display the final test DataFrame
print(test_snp_df.head(20))
