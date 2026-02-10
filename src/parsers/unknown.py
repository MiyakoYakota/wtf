# Generic parser for unknown text formats. It will make the best attempt to extract data using regex.

from utils.logs import logger
from parsers.base_parser import BaseParser
from ir.record import Record

class UnknownParser(BaseParser):
    _EXTENSIONS = []
    _IS_WILDCARD = True

    def get_itr(self):
        with open(self.file_path, 'r') as f:
            for line in f:
                ir = Record()
                yield ir.to_dict()