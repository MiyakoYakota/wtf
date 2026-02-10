import json
import os

mappings_path = os.path.join(os.path.dirname(__file__), 'mappings.json')
mappings = json.load(open(mappings_path, 'r'))

def get_mapping(key):
    if key in mappings:
        return key
    
    lower = key.lower()
    
    for k, v in mappings.items():
        if lower in v:
            return k
    

    return None