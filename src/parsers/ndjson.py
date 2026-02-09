from .base_parser import BaseParser
import json

class NDJSONParser(BaseParser):
    _EXTENSIONS = ['.ndjson', '.jsonl']

    def get_itr(self):
        with open(self.file_path, 'r') as f:
            for line in f:
                yield line.strip()

    def parse(self):
        for line in self.get_itr():
            print(line)