from utils.logs import get_logger

logger = get_logger(__name__)

logger.info("Loading Postal address parser, please be patient...")
from postal.parser import parse_address
from postal.normalize import normalize_string
logger.info("Postal address parser loaded successfully.")

usStates = [
    'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware',
    'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky',
    'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana',
    'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio',
    'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas',
    'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming', 'washington dc', 'district of columbia'

    "al", "ak", "az", "ar", "ca", "co", "ct", "de",
    "fl", "ga", "hi", "id", "il", "in", "ia", "ks", "ky",
    "la", "me", "md", "ma", "mi", "mn", "ms", "mo", "mt",
    "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh",
    "ok", "or", "pa", "ri", "sc", "sd", "tn", "tx",
    "ut", "vt", "va", "wa", "wv", "wi", "wy", "dc"

    # territories
    "puerto rico", "pr",
    "guam", "gu",
    "american samoa", "as",
    "northern mariana islands", "mp",
    "virgin islands", "vi",
]

def extract(address: str, original_key: str, original_dict: dict):
    fields = [
        'house_number',
        'road',
        'unit',
        'pobox',
        'city',
        'state',
        'country',
        'postcode'
    ]
    
    newAddressString = address

    if 'city' in original_dict and original_dict['city'] not in address:
        newAddressString += f", {original_dict['city']}"
    
    if 'state' in original_dict and original_dict['state'] not in address:
        newAddressString += f", {original_dict['state']}"
    
    if 'country' in original_dict and original_dict['country'] not in address:
        newAddressString += f", {original_dict['country']}"

    if 'country' not in original_dict and 'state' in original_dict and original_dict['state'].lower() in usStates:
        newAddressString += ", USA"

    if 'zipCode' in original_dict and original_dict['zipCode'] not in address:
        newAddressString += f", {original_dict['zipCode']}"
        
    results = [{
        'address': normalize_string(newAddressString)
    }]

    parsed = parse_address(newAddressString)

    # Map libpostal components to our desired output
    for component, label in parsed:
        if label in fields:
            #convert to camelCase
            fieldName = ''.join(word.capitalize() for word in label.split('_'))
            fieldName = fieldName[0].lower() + fieldName[1:]
            results.append({fieldName: component})
    
    return results