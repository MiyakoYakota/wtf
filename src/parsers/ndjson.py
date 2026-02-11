import json

from utils.logs import get_logger

logger = get_logger(__name__)
from .base_parser import BaseParser

class NDJSONParser(BaseParser):
    _EXTENSIONS = ['.ndjson', '.jsonl']

    def get_itr(self):
        with open(self.file_path, 'r') as f:
            for line in f:
                yield json.loads(line.strip())
