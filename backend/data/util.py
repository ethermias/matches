import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json_file(file_path, my_dict):
    with open(file_path, "w") as file:
        json.dump(my_dict, file)