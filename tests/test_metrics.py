import numpy as np
import pandas as pd

from rag_finance.evaluate import bootstrap_ci, summarize


def _cas():
    # 4 questions : bonne page au rang 1, 3, 7, et jamais trouvée
    return pd.DataFrame({"page_rank": [1, 3, 7, np.inf], "doc_rank": [1, 1, 2, np.inf]})


def test_recall_at_k():
    s = summarize(_cas())
    assert s["recall@1"] == 0.25
    assert s["recall@3"] == 0.5
    assert s["recall@10"] == 0.75


def test_mrr():
    s = summarize(_cas())
    assert abs(s["MRR"] - (1 + 1 / 3 + 1 / 7) / 4) < 1e-9


def test_bootstrap_encadre_la_moyenne():
    hits = [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]
    lo, hi = bootstrap_ci(hits)
    assert lo <= np.mean(hits) <= hi
    assert 0.0 <= lo <= hi <= 1.0
