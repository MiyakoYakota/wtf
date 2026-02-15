from src.ingest import *
import subprocess

"""

map in head:
1. check data/
2. use wtf via subprocess to execute:
    - venv_python_interpreter wtf_path wtf_flags 
3. check src/ingest/data/ for validated JSONL 
4. use ingest (from src.ingest import ingest) to ingest directly into datastore

"""