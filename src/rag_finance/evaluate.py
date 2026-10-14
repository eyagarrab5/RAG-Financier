"""Métriques de retrieval : recall@k, MRR, intervalle de confiance bootstrap."""
import numpy as np
import pandas as pd

from .config import KS, SEED


def summarize(rk: pd.DataFrame, ks=KS) -> dict:
    """rk contient les colonnes page_rank et doc_rank (np.inf si non trouvé)."""
    out = {f"recall@{k}": float((rk.page_rank <= k).mean()) for k in ks}
    out["MRR"] = float(np.where(np.isfinite(rk.page_rank), 1.0 / rk.page_rank, 0.0).mean())
    out["doc_hit@10"] = float((rk.doc_rank <= 10).mean())
    return out


def bootstrap_ci(hits, n_boot: int = 2000, seed: int = SEED):
    """Intervalle de confiance à 95 % de la moyenne d'un vecteur de 0/1."""
    hits = np.asarray(hits, dtype=float)
    rng = np.random.default_rng(seed)
    means = [rng.choice(hits, size=len(hits), replace=True).mean() for _ in range(n_boot)]
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))
