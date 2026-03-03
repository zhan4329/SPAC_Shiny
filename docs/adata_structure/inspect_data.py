'''
This script is designed to inspect the contents of an AnnData object
loaded from a pickle file.

Run commands under this directory to explore the AnnData object:
python -mpickle ../../dev_example.pickle
python inspect_data.py
'''

import pickle
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.parent

# 1. Load the AnnData object from the pickle file
# Make sure you are in the same directory as 'dev_example.pickle'
with open(ROOT_PATH / 'dev_example.pickle', 'rb') as f:
    adata = pickle.load(f)

# 2. Print the overall shape (Number of Cells x Number of Features)
print("--- Shape of the dataset (cells, features) ---")
print("adata.shape:", adata.shape)
print("adata.X.shape:", adata.X.shape)
print("adata.obs.shape:", adata.obs.shape) 
print("adata.var.shape:", adata.var.shape)
print("adata.obsm['spatial'].shape:", adata.obsm['spatial'].shape)
print("adata.obsm['spatial'].dtype:", adata.obsm['spatial'].dtype)
print("\n")

# 3. Print the first 5 rows of the cell metadata (like cell types)
print("--- First 5 rows of cell metadata (adata.obs) ---")
print(adata.obs.head())
print("\n")

# 4. Print the spatial coordinates for the first 5 cells
print("--- Spatial coordinates of the first 5 cells (adata.obsm['spatial']) ---")
print(adata.obsm['spatial'][:5])
print("\n")

# 5. Print the actual expression values (adata.X) for the first 5 cells and first 5 features
print("--- Expression matrix for first 5 cells & 5 features (adata.X) ---")
print(adata.X[:5, :5])