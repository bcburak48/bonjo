from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def cluster_users(user_venue_time, n_clusters=5):
    scaler = StandardScaler()
    user_venue_time_scaled = scaler.fit_transform(user_venue_time)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(user_venue_time_scaled)
    return clusters


def cluster_users_weighted(user_venue_time_weighted, n_clusters=5):
    scaler = StandardScaler()
    user_venue_time_weighted_scaled = scaler.fit_transform(user_venue_time_weighted)
    kmeans_weighted = KMeans(n_clusters=n_clusters, random_state=42)
    clusters_weighted = kmeans_weighted.fit_predict(user_venue_time_weighted_scaled)
    return clusters_weighted
