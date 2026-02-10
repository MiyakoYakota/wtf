from utils.logs import logger

logger.info("Loading Postal address parser, please be patient...")
from postal.parser import parse_address
from postal.normalize import normalize_string
logger.info("Postal address parser loaded successfully.")

def extract(address: str):
    fields = [
        'house_number',
        'road',
        'unit',
        'pobox',
        'city',
        'state',
        'country'
    ]

    result = {
        'address': normalize_string(address)
    }

    # Use libpostal to parse the address
    parsed = parse_address(address)

    # Map libpostal components to our desired output
    for component, label in parsed:
        if label in fields:
            #convert to camelCase
            fieldName = ''.join(word.capitalize() for word in label.split('_'))
            fieldName = fieldName[0].lower() + fieldName[1:]
            result[fieldName] = component
    
    return result