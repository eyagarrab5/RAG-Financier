"""Configuration centrale : tous les paramètres au même endroit."""
from pathlib import Path

SEED = 42

# sélection des documents
N_PAIR_COMPANIES = 6
N_SINGLES = 6

# découpage
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200
ADD_HEADER = True

# modèles
EMB_MODEL = "BAAI/bge-base-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
RERANK_MODEL = "BAAI/bge-reranker-base"

# retrieval
TOP_N = 50
RERANK_TOP = 30
RRF_K = 60

# évaluation
KS = [1, 3, 5, 10]
DEV_FRAC = 0.7

# chemins
REPO_ROOT = Path(__file__).resolve().parents[2]
EVAL_DIR = REPO_ROOT / "eval"
RESULTS_DIR = REPO_ROOT / "results"
