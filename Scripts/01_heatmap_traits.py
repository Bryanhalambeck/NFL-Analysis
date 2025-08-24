"""
01_heatmap_traits.py
---------------------
Generates a heatmap of average z-score traits by Vegas result group.

Input:
    data/nfl-analysis-data.csv 

Output:
    charts/heatmap_traits_by_group.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Config
# =========================
DATA_FILE = "data/nfl-analysis-data.csv"
CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)

# =========================
# Load Data
# =========================
df = pd.read_csv(DATA_FILE)

if "Vegas_Result_Group" not in df.columns:
    raise ValueError("❌ Vegas_Result_Group column not found. Run 00_label_results.py first.")

# =========================
# Heatmap of traits by Result Group
# =========================
metrics_to_plot = [
    'Total_DVOA_zscore','Off_DVOA_zscore','Def_DVOA_zscore',
    'ST_DVOA_zscore','Sched%_zscore','No1_Pick_Odds_zscore',
    'Playoff_Odds_zscore','SB_Win_Odds_zscore','FPI_Total_zscore',
    'FPI_Off_zscore','FPI_Def_zscore','Luck_Z','Age_Z',
    'SRS_zscore','OSRS_zscore','DSRS_zscore','Momentum_Z','SOS_zscore'
]

df_clean = df[['Vegas_Result_Group'] + metrics_to_plot]
group_means = df_clean.groupby("Vegas_Result_Group")[metrics_to_plot].mean().T

plt.figure(figsize=(12,10))
sns.heatmap(group_means, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Average Z-Score Traits by Vegas Accuracy Group")
plt.xlabel("Vegas Result Group")
plt.ylabel("Z-Score Metric")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/heatmap_traits_by_group.png")
plt.show()

print("✅ Heatmap saved to charts/heatmap_traits_by_group.png")
