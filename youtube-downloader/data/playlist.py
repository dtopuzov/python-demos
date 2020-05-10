import json
import os


def get_playlist():
    script_path = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(script_path, "playlist.json")
    with open(json_path, "r") as f:
        return json.load(f)['playlist']


def __read_data():
    script_path = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(script_path, "playlist.json")
    with open(json_path, "r") as f:
        return json.load(f)
