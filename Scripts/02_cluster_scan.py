"""
02_cluster_scan.py
------------------
Scans metric combinations to find KMeans clusters that are highly
Overrated or Underrated based on Vegas_Result_Group proportions.

Input:
    data/nfl-analysis-data.csv

Output:
    outputs/high_signal_clusters.csv
    Console printout of top clusters
"""

import os
import pandas as pd
from itertools import combinations
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# =========================
# Config
# =========================
DATA_FILE   = "data/nfl-analysis-data.csv"
OUTPUT_DIR  = "outputs"
SEED        = 42
N_CLUSTERS  = 3

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# Load Data
# =========================
df = pd.read_csv(DATA_FILE)

if "Vegas_Result_Group" not in df.columns:
    raise ValueError("❌ Vegas_Result_Group column not found. Run 00_label_results.py first.")

# =========================
# Metric Tiers (adjust as needed)
# =========================
tier_a = ['Age_Z']
tier_b = ['Playoff_Odds_zscore', 'Sched%_zscore', 'DSRS_zscore', 'Off_DVOA_zscore']
tier_c = ['Total_DVOA_zscore', 'OSRS_zscore', 'FPI_Def_zscore', 'No1_Pick_Odds_zscore', 'Momentum_Z']

all_metrics = [m for m in (tier_a + tier_b + tier_c) if m in df.columns]

# Signal thresholds by combo size
thresholds = {2: 0.47, 3: 0.50, 4: 0.53}

# =========================
# Scan Combinations
# =========================
rows = []
for r in [2, 3, 4]:
    for combo in combinations(all_metrics, r):
        cols = list(combo) + ["Vegas_Result_Group"]
        if any(c not in df.columns for c in cols):
            continue

        df_cluster = df[cols].dropna().copy()
        if df_cluster.shape[0] < 10:
            continue

        X = StandardScaler().fit_transform(df_cluster[list(combo)])
        kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=SEED, n_init="auto")
        df_cluster["Cluster"] = kmeans.fit_predict(X)

        counts = pd.crosstab(df_cluster["Cluster"], df_cluster["Vegas_Result_Group"])
        props = counts.div(counts.sum(axis=1), axis=0)

        for cluster_id, row in props.iterrows():
            for label in ["Overrated", "Underrated"]:
                if row.get(label, 0) >= thresholds[r]:
                    rows.append({
                        "Metrics": ", ".join(combo),
                        "Cluster": int(cluster_id),
                        "Label": label,
                        "Percent": round(float(row[label]), 3),
                        "N_in_cluster": int(counts.loc[cluster_id].sum())
                    })

# =========================
# Results
# =========================
results = pd.DataFrame(rows).sort_values(by=["Percent", "N_in_cluster"], ascending=False)

if results.empty:
    print("No clusters crossed the thresholds. Try different metrics/thresholds.")
else:
    print("\n📊 High-Signal Clusters (Sorted by Signal Strength):\n")
    print(results.to_string(index=False))

results.to_csv(f"{OUTPUT_DIR}/high_signal_clusters.csv", index=False)
print(f"\n✅ Saved results to {OUTPUT_DIR}/high_signal_clusters.csv")
