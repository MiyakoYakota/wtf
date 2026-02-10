import os
import logging
import argparse
from utils.load_parsers import load_parsers
from utils.logs import logger
from parsers import base_parser


def main():
    logger.info("Starting WTF parser")
    parsers = load_parsers()

    argparser = argparse.ArgumentParser(description='WTF Parser')
    argparser.add_argument('file', help='The file to parse')

    argparser.add_argument('-o', '--output', help='Output file path', required=False)
    argparser.add_argument('-p', '--parser', help='Specify which parser to use', choices=parsers.keys(), required=False)
    argparser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')

    args = argparser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")

    logger.debug(f"Loaded {len(parsers)} parser(s)")

    print(f"Parsing file: {args.file}")

    if args.parser:
        parser_class = parsers[args.parser]
        logger.info(f"Using specified parser: {args.parser}")
    else:
        file_extension = os.path.splitext(args.file)[1].lower()
        parser_class = None
        for _, cls in parsers.items():
            if file_extension in cls._EXTENSIONS:
                parser_class = cls
                logger.info(f"Auto-detected parser: {cls.__name__} for extension {file_extension}")
                break

        if not parser_class:
            logger.error(f"No parser found for file extension: {file_extension}")
            return

    parser = parser_class(args.file)
    parser.parse()

if __name__ == "__main__":
    main()