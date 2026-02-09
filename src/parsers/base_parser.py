class BaseParser:
    _EXTENSIONS = []

    def __init__(self, file_path):
        self.file_path = file_path

    def get_itr(self):
        raise NotImplementedError("Subclasses must implement the get_itr method")

    def parse(self):
        raise NotImplementedError("Subclasses must implement the parse method")