# SilverFiche

SilverFiche is a full‑stack semantic book recommender powered by vector embeddings, zero‑shot classification, and sentiment analysis. It includes a complete vocabulary module where users can store words, view detailed definitions, and track mastery.


## Features

- Content-based book recommendations using semantic search
- Topic and category classification for books
- Emotional tone analysis for book descriptions
- Vocabulary section where readers:
  - Save words they find difficult or interesting
  - Attach words to specific books and sentences
  - View detailed word pages (definition, pronunciation, examples)
  - Practice and track mastery over time

## Tech Stack

- Backend: Python (FastAPI or Flask)
- Frontend: HTML, CSS, JavaScript
- NLP / LLM:
  - OpenAI embeddings (or other embedding models)
  - HuggingFace Transformers for classification and sentiment
- Vector search: ChromaDB or FAISS
- Database: PostgreSQL or SQLite

## Project Structure

```text
silverfiche/
│
├── app/
│   ├── main.py
│   ├── recommender.py
│   ├── vocab.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── vocab_list.html
│   │   ├── vocab_word.html
│   │   └── books.html
│   └── static/
│       ├── css/
│       │   └── theme.css
│       └── img/
│           └── logo.svg
├── models/
│   ├── db_schema.sql
│   └── nlp_config.py
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── embeddings/
├── README.md
└── requirements.txt
