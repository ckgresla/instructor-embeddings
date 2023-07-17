# Helper Functions for interacting with Data (on disk or otherwise)

import io
import json
import os
from typing import List, Dict




# ---- LOCAL FILE SYSTEM FUNCTIONS ----

# Extract Dicts from Local File Paths
def read_json_data(filepath):
    if os.path.exists(filepath):
        file = io.open(filepath, mode="r", encoding="utf-8")
        data = json.load(file)
        file.close()
        return data #dictionary for parsing/uploading
    else:
        print(f"File: '{filepath}' doesn't seem to exist, returning empty dictionary")
        return {} #base for creating any new data dicts (writer util can work with one entry)

# Write out JSONs w Human-Readable indents
def write_json_data(filepath, data):
    with io.open(filepath, mode="w", encoding="utf-8") as f:
        file = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(file)
        f.close()

def write_txt_data(filepath, data):
    """ Dump a String to a text file, should refactor if ever using """
    with io.open(filepath, mode="w", encoding="utf-8") as f:
        f.write(data)
        f.close()

def read_jsonl_data(filepath: str) -> List[Dict]:
    if os.path.exists(filepath):
        data = []
        file = io.open(filepath, mode="r", encoding="utf-8")
        for line in file:
            data.append(json.loads(line))
        file.close()
        return data #list of dicts per line in JSON
    else:
        print(f"File: '{filepath}' doesn't seem to exist")
        return {}

def write_jsonl_data(filepath: str, data: List[Dict]):
    with open(filepath, mode="w", encoding="utf-8") as f:
        # Write out all provided lines
        for jeh_son in data:
            # json.dump(jeh_son, f, ensure_ascii=False)
            f.write(json.dumps(dict(jeh_son), separators=(',', ':')))
            f.write("\n") #newlines must be verbosely written in JSONL
        f.close()

