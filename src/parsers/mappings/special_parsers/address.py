from postal.parser import parse_address


def convert_address_string_to_parts(address: str):
    # Initialize the result dictionary with default None values
    result = {
        'street': None,
        'city': None,
        'state': None,
        'zip_code': None,
        'country': None
    }

    # Use libpostal to parse the address
    parsed = parse_address(address)

    # Map libpostal components to our desired output
    for component, label in parsed:
        print(f"Component: {component}, Label: {label}")