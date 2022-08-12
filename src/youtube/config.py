import os 
import json 

CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'config/properties.json')
with open(CONFIG_FILE) as f:
    config = json.load(f)