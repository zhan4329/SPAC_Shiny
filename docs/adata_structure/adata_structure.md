### Output of `python -mpickle ../../dev_example.pickle`

AnnData object with n_obs × n_vars = 4825 × 33
    obs: 'broad_cell_type', 'detailed_cell_type', 'manual_phenotype', 'phenograph_k60_r1', 'renamed_clusters', 'CD3Dspatial_plot', 'CD20spatial_plot'
    uns: 'phenograph_features', 'phenograph_k60_r1_colors', 'renamed_clusters_colors', '_spac_palettes', 'spatial_neighbors', 'renamed_clusters_plot_nhood_enrichment', 'ripley_l_with_edge', 'ripley_l_without_edge', 'ripley_l'
    obsm: 'spatial', 'X_umap', 'spatial_distance'
    layers: 'arcsinh_percentile', 'arcsinh_z_scores'
    obsp: 'spatial_connectivities', 'spatial_distances'

### Output of `python inspect_data.py`

--- Shape of the dataset (cells, features) ---
adata.shape: (4825, 33)
adata.X.shape: (4825, 33)
adata.obs.shape: (4825, 7)
adata.var.shape: (33, 0)
adata.obsm['spatial'].shape: (4825, 2)
adata.obsm['spatial'].dtype: float32


--- First 5 rows of cell metadata (adata.obs) ---
  broad_cell_type         detailed_cell_type  ... CD3Dspatial_plot CD20spatial_plot
0         B Cells                     B Cell  ...        -0.996883         1.709721
1         B Cells  Follicular Dendritic Cell  ...        -0.971774         0.582074
2         B Cells  Follicular Dendritic Cell  ...        -0.940262         0.866047
3         B Cells                     B Cell  ...        -1.481576         1.338160
4         B Cells  Follicular Dendritic Cell  ...        -1.380023         0.666479

[5 rows x 7 columns]


--- Spatial coordinates of the first 5 cells (adata.obsm['spatial']) ---
[[511.55554    9.846154]
 [579.3301     9.398058]
 [630.9583    12.883333]
 [745.19464   16.275167]
 [657.17365   18.035929]]


--- Expression matrix for first 5 cells & 5 features (adata.X) ---
[[ 581.5811966  618.3846154 1606.777778   509.3247863  477.5897436]
 [ 565.8932039  442.2912621 1539.398058   496.8252427  484.9029126]
 [ 666.475      574.3333333 1759.683333   548.05       494.1666667]
 [ 558.5033557  408.5771812 1557.738255   472.3691275  347.0939597]
 [ 562.         524.4550898 1596.982036   482.0658683  372.8982036]]