import os
import sys
import json

sys.path.insert(0, "src")

os.makedirs("data",              exist_ok=True)
os.makedirs("artifacts",         exist_ok=True)
os.makedirs("artifacts/rings",   exist_ok=True)

print("=" * 55)
print("  FRAUD DETECTION SYSTEM — FULL PIPELINE")
print("=" * 55)

print("\n Loading datasets ...")
from etl import load_creditcard, load_paysim, split

cc_df = load_creditcard()
ps_df = load_paysim()

PS_SAMPLE = 20000
if len(ps_df) > PS_SAMPLE:
    print(f"  Using {PS_SAMPLE:,} row sample of PaySim (edit main.py to use full dataset)")
    ps_sample = ps_df.sample(n=PS_SAMPLE, random_state=42)
else:
    ps_sample = ps_df

print("\n Building transaction graph ...")
import graph_builder as gb

G, metrics, partition, comm_stats = gb.run(ps_sample)

print("\nEngineering features ...")
from features import (
    creditcard_features, graph_node_features, get_graph_Xy
)
cc_X, cc_y, cc_cols = creditcard_features(cc_df)

with open("data/node_metrics.json")    as f: node_met   = json.load(f)
with open("data/community_stats.json") as f: comm_stats = json.load(f)

feat_df = graph_node_features(ps_sample, node_met, comm_stats)
gr_X, gr_y, gr_cols = get_graph_Xy(feat_df)

print("\nSTEP 4 — Training models ...")
from sklearn.model_selection import train_test_split
from train import train_creditcard, train_graph

cc_df_nonan = cc_df.dropna(subset=cc_cols + ["Class"])
Xtr_cc, Xte_cc, ytr_cc, yte_cc = train_test_split(
    cc_df_nonan[cc_cols], cc_df_nonan["Class"],
    test_size=0.2, stratify=cc_df_nonan["Class"], random_state=42
)
best_cc = train_creditcard(Xtr_cc, ytr_cc, Xte_cc, yte_cc, cc_cols)

Xtr_g, Xte_g, ytr_g, yte_g = train_test_split(
    gr_X, gr_y, test_size=0.2, stratify=gr_y, random_state=42
)
best_gr = train_graph(Xtr_g, ytr_g, Xte_g, yte_g, gr_cols)

print("\nDetecting fraud rings ...")
from ring_detector import detect_rings, business_metrics

rings = detect_rings(G, comm_stats, min_size=3, min_risk=0.10)
biz   = business_metrics(rings, ps_sample)

print("\n" + "=" * 55)
print("  PIPELINE COMPLETE")
print("=" * 55)
