
- **data/**: Directory for raw data files.
- **notebooks/**: Directory for Jupyter Notebook files for data analysis and visualization.
- **src/**: Main directory for project Python modules.
  - **classification.py**: Functions for user classification.
  - **clustering.py**: Clustering algorithms for grouping users.
  - **data_loader.py**: Functions for data loading and preprocessing.
  - **feature_engineering.py**: Functions for feature engineering.
  - **visualization.py**: Functions for data visualization.
- **requirements.txt**: List of project dependencies.
- **README.md**: Project overview and instructions.

## Usage

The project is structured to be run in a Jupyter Notebook environment. Open `notebooks/data_analysis.ipynb` and execute the cells step by step. Follow the steps below:

### Jupyter Notebook Steps

1. **Install the Required Libraries:**

    ```python
    !pip install -r ../requirements.txt
    ```

2. **Add `src` Directory to Python Path:**

    ```python
    import sys
    import os

    project_root = os.path.abspath("..")
    src_path = os.path.join(project_root, "src")
    sys.path.append(src_path)
    ```

3. **Load and Visualize the Data:**

    ```python
    from data_loader import load_data
    from visualization import plot_venue_visits, plot_visits_over_time

    file_path = "../data/time_series_classification_data_100.json"
    df = load_data(file_path)

    plot_venue_visits(df)
    plot_visits_over_time(df)
    ```

4. **Cluster Users Based on Visit Behavior:**

    ```python
    from feature_engineering import create_features
    from clustering import cluster_users

    user_venue_time = create_features(df)
    clusters = cluster_users(user_venue_time, n_clusters=5)
    df['cluster'] = df['user'].map(dict(zip(user_venue_time.index, clusters)))
    ```

5. **Cluster Users with Weighted Visit Behavior:**

    ```python
    from feature_engineering import create_weighted_features
    from clustering import cluster_users_weighted

    user_venue_time_weighted = create_weighted_features(df)
    clusters_weighted = cluster_users_weighted(user_venue_time_weighted, n_clusters=5)
    df['cluster_weighted'] = df['user'].map(dict(zip(user_venue_time_weighted.index, clusters_weighted)))
    ```

6. **Classify Users:**

    ```python
    from classification import classify_users

    user_classifications = classify_users(df)
    print(user_classifications)
    ```
