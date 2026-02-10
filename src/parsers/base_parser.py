import parsers.mappings.mappings

from utils.logs import logger


class BaseParser:
    _EXTENSIONS = []

    def __init__(self, file_path):
        self.file_path = file_path

    def associate_key(self, key):
        return parsers.mappings.mappings.get_mapping(key)

    def get_itr(self):
        raise NotImplementedError("Subclasses must implement the get_itr method")

    def parse(self):
        for record in self.get_itr():
            try:
                for key, value in record.items():
                    mapped_key = self.associate_key(key)
                    if mapped_key:
                        logger.info(f"{mapped_key}: {value}")
                    else:
                        logger.warning(f"Unmapped key: {key}")

            except Exception as e:
                logger.error(f"Error parsing record: {record}\nError: {e}")