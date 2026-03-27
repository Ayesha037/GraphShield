GraphShield — Transaction Graph Intelligence & Fraud Ring Detection
A graph-based fraud intelligence platform that detects organized fraud rings at scale by analyzing entity relationship networks using community detection and node embeddings.

Problem Statement
Traditional rule-based fraud detection misses organized fraud rings — groups of accounts working together to commit fraud. By modeling transactions as a graph, hidden patterns invisible to row-level ML models become detectable.

Tech Stack
CategoryToolsLanguagePythonGraph AnalyticsNetworkX, Community Detection AlgorithmsNode Embeddingsnode2vecVisualizationInteractive Network GraphsLibrariesPandas, NumPy, Matplotlib

Key Features

Graph Modeling — Entities (accounts, devices, IPs) modeled as nodes; transactions as edges
Community Detection — Identifies tightly connected fraud clusters using graph community algorithms
node2vec Embeddings — Encodes transaction graph topology for unsupervised fraud cluster discovery
Interactive Visualizations — Network graphs support fraud investigation workflows, reducing manual case review
Scalable Design — Architected to process millions of transaction edges for large-scale payment networks


How It Works
Raw Transactions
      ↓
Graph Construction (entities = nodes, transactions = edges)
      ↓
node2vec Embeddings (encode graph topology)
      ↓
Community Detection (find fraud rings)
      ↓
Interactive Visualization (investigate clusters)
 How to Run
bash# Clone the repo
git clone https://github.com/Ayesha037/GraphShield.git
cd GraphShield

# Install dependencies
pip install -r requirements.txt

# Run the main script
python main.py

 Project Structure
GraphShield/
│
├── data/                  # Transaction data
├── graph/                 # Graph construction modules
├── embeddings/            # node2vec embedding logic
├── detection/             # Community detection algorithms
├── visualizations/        # Network graph visualizations
├── requirements.txt
└── README.md

 Results

Detected organized fraud rings invisible to row-level models
Interactive investigation dashboard reduces manual case review effort
Scales to millions of transaction edges


 Key Learnings

Graph-based approaches catch fraud patterns that tabular ML completely misses
node2vec embeddings are powerful for encoding relational structure in unsupervised settings
Visualization is critical for fraud investigators — explainability matters as much as accuracy


 Author
Mohammad Ayesha Summaiyya
msumaiya03579@gmail.com
