import json
from pprint import pprint

# Load the JSON file
with open('serverdata\djid_app\jsondata.json', 'r') as file:
    data = json.load(file)

# Extract unique words from specified fields
fields_to_extract = ['end_year', 'topic', 'sector', 'region', 'pestle', 'source', 'country', 'city', 'SWOT']
unique_words = set()

for item in data:
    for field in fields_to_extract:
        field_value = item.get(field)
        if isinstance(field_value, str):  # Check if the field's value is a string
            words = field_value.split()
            unique_words.update(words)

# Print unique words
pprint(unique_words)