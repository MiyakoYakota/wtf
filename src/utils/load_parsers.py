import os
import importlib

from utils.logs import logger
from parsers import base_parser

def load_parsers():
    parsers_dir = os.path.join(os.path.dirname(__file__), '..', 'parsers')
    parsers = {}
    for filename in os.listdir(parsers_dir):
        if filename.endswith('.py') and filename not in ('base_parser.py', '__init__.py'):
            module_name = f"parsers.{filename[:-3]}"
            try:
                module = importlib.import_module(module_name)
                parser_class = None
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and issubclass(attr, base_parser.BaseParser) and attr != base_parser.BaseParser:
                        logger.info(f"Loaded parser class {attr_name} from {filename}")
                        parsers[filename] = attr
                        break
                if parsers[filename] is None:
                    raise ValueError(f"No parser class found in {filename}")
                
            except Exception as e:
                logger.error(f"Error loading parser from {filename}: {e}")

    return parsers