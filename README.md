# GraphShield — Transaction Graph Intelligence & Fraud Ring Detection

A graph-based fraud intelligence platform that detects **organised fraud rings** by modelling entity relationships as a network and applying community detection and node embeddings.

Traditional row-level ML misses fraud rings. GraphShield doesn't.

## What it does

* Models accounts, devices, and IPs as nodes; transactions as edges
* Applies node2vec to encode graph topology as embeddings
* Runs community detection to surface tightly connected fraud clusters
* Generates interactive network visualisations for fraud investigator workflows
* Scales to millions of transaction edges

## Tech Stack
Python, NetworkX, node2vec, Community Detection Algorithms, Pandas, NumPy, Matplotlib

## Pipeline Structure
Raw Transactions → Graph Construction → node2vec Embeddings → Community Detection → Interactive Visualisation

## How to Run

```bash
git clone https://github.com/Ayesha037/GraphShield.git
cd GraphShield
pip install -r requirements.txt
python main.py
```

## Project Structure
GraphShield/
├── main.py               # Entry point
├── graph/                # Graph construction modules
├── embeddings/           # node2vec embedding logic
├── detection/            # Community detection algorithms
├── visualizations/       # Network graph visualisations
└── requirements.txt

## Key Learnings

* Graph approaches catch fraud patterns that tabular ML completely misses
* node2vec embeddings are powerful for relational structure in unsupervised settings
* Visualisation is critical — explainability matters as much as accuracy for investigators

## Author
**Mohammad Ayesha Summaiyya** — msumaiya03579@gmail.com
