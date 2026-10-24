# Financial Document Analysis with Retrieval-Augmented Generation (RAG)

## Overview

Financial reports such as 10-K, 10-Q, and 8-K filings contain large amounts of information that can be difficult and time-consuming to navigate when answering specific financial questions.

This project explores **Retrieval-Augmented Generation (RAG)** and information retrieval techniques to identify relevant evidence from financial documents. Rather than relying solely on a language model's internal knowledge, the system focuses on retrieving relevant document passages that can support answers to financial questions.

The project is being developed independently to explore practical applications of Large Language Models (LLMs) and strengthen hands-on experience in information retrieval, semantic search, and retrieval evaluation.

## Objectives

- Build a retrieval pipeline for searching financial reports.
- Extract and preprocess text from PDF documents.
- Compare keyword-based, vector-based, and hybrid retrieval methods.
- Investigate reranking techniques to improve the relevance of retrieved passages.
- Evaluate retrieval quality using standard information retrieval metrics.
- Analyze retrieval errors to identify limitations and opportunities for improvement.

## Dataset

The project uses **FinanceBench**, a benchmark designed for evaluating question answering over financial documents.

The dataset includes:

- **150 financial questions**
- **361 financial documents**

The benchmark provides a practical setting for evaluating whether retrieval methods can locate relevant evidence needed to answer financial questions.

## Methodology

### 1. PDF Extraction and Preprocessing

Financial reports are processed using PyMuPDF to extract text at the page level.

The extracted content is divided into overlapping chunks to preserve useful context while making retrieval more efficient.

Current chunking configuration:

- **Chunk size:** 1,200 characters
- **Chunk overlap:** 200 characters
- **Extraction:** Page-level PDF text processing

### 2. Text Embeddings and Vector Storage

Dense vector representations are generated using the `BAAI/bge-base-en-v1.5` embedding model.

The embeddings are stored in **ChromaDB**, enabling semantic similarity search across financial document passages.

This approach aims to retrieve passages based on their semantic relevance, even when the wording of a query differs from the original document.

### 3. Retrieval Strategies

The project implements and compares multiple retrieval approaches.

| Method | Description |
|---|---|
| BM25 | Keyword-based retrieval using lexical matching |
| Dense Vector Search | Retrieves passages based on semantic similarity |
| Hybrid Retrieval | Combines keyword-based and dense vector retrieval |
| Hybrid Retrieval + Reranking | Reorders retrieved passages using a reranking stage to improve relevance |

Comparing these approaches helps investigate the trade-offs between exact keyword matching and semantic understanding in financial document retrieval.

### 4. Experimental Evaluation

The evaluation workflow uses a development/test split:

- **Development set:** 70%
- **Test set:** 30%

The development set supports experimentation and comparison between retrieval strategies, while the test set is reserved for evaluating retrieval performance.

### 5. Evaluation Metrics

Retrieval quality is evaluated using:

- **Recall@k:** Measures whether relevant evidence appears among the top *k* retrieved passages.
- **Mean Reciprocal Rank (MRR):** Measures how highly the first relevant result is ranked.

These metrics help assess both the coverage and ranking quality of retrieved evidence.

### 6. Error Analysis

Error analysis is used to investigate retrieval failures, including cases where relevant passages are not retrieved or are ranked too low.

The findings can help guide improvements to chunking, retrieval strategies, and reranking.

## Technologies

- **Language:** Python
- **PDF Processing:** PyMuPDF
- **Embeddings:** BAAI/bge-base-en-v1.5
- **Vector Database:** ChromaDB
- **Retrieval:** BM25, dense vector search, hybrid retrieval
- **Evaluation:** Recall@k, MRR
- **Concepts:** RAG, LLM applications, semantic search, information retrieval, reranking

## Current Status

**In progress.**

The current focus is implementing the retrieval pipeline, comparing retrieval strategies, and evaluating their performance on FinanceBench. Further improvements will be guided by experimental results and error analysis.

## Future Improvements

Potential next steps include:

- Fine-tuning chunking strategies for financial documents.
- Experimenting with different embedding models.
- Testing alternative hybrid retrieval configurations.
- Evaluating different reranking models.
- Investigating retrieval failures by question type and document structure.
- Integrating a language model to generate answers grounded in retrieved evidence.
- Assessing answer quality and factual consistency in addition to retrieval performance.

## Key Takeaways

This project provides hands-on experience with:

- Building a document retrieval pipeline for financial reports.
- Processing PDF documents and designing text chunking strategies.
- Implementing keyword-based and semantic retrieval.
- Combining retrieval methods and investigating reranking.
- Evaluating search quality using information retrieval metrics.
- Conducting systematic experiments and error analysis.

## Project Information

- **Project type:** Personal project
- **Domain:** Financial document analysis
- **Main focus:** Retrieval-Augmented Generation and information retrieval
- **Dataset:** FinanceBench
- **Status:** In progress

---

*This project focuses on implementing and evaluating retrieval methods. Full answer generation and end-to-end RAG evaluation should be described as completed only once those components have been implemented and tested.*
