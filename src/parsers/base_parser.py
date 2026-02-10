import parsers.mappings.mappings

from ir.record import Record
from utils.logs import logger


class BaseParser:
    _EXTENSIONS = []

    def __init__(self, file_path):
        self.file_path = file_path

    def associate_key(self, key):
        return parsers.mappings.mappings.get_mapping(key)

    def parse_value(self, key, value):
        return parsers.mappings.mappings.get_value(key, value)

    def get_itr(self):
        raise NotImplementedError("Subclasses must implement the get_itr method")

    def parse(self):
        for record in self.get_itr():
            try:
                std_record = Record()
                for key, value in record.items():
                    mapped_key = self.associate_key(key)
                    values = self.parse_value(mapped_key, value) if mapped_key else None

                    if not values:
                        # logger.warning(f"Unmapped key: {key} with value: {value}")
                        continue

                    # for newValue in values:
                    #     for k, v in newValue.items():
                    #         print(f"{k}: {v}")
                    
                    # if mapped_key:
                    #     logger.info(f"{mapped_key}: {value}")
                    # else:
                    #     logger.warning(f"Unmapped key: {key}")

            except Exception as e:
                logger.error(f"Error parsing record: {record}\nError: {e}")