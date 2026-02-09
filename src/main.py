import os
import importlib
import argparse
from utils.load_parsers import load_parsers
from utils.logs import logger
from parsers import base_parser


def main():
    logger.info("Starting WTF parser")
    parsers = load_parsers()

    logger.info(f"Loaded {len(parsers)} parser(s)")

if __name__ == "__main__":
    main()