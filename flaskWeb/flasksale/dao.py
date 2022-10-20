import json
from flasksale import app


def load_categories():
    with open(f'{app.route_path}/data/categories.json', encodings='utf-8') as f:
        return json.load;