import json

def json_write(json_file_path, text):
    with open(json_file_path, 'w') as file:
        json.dump({'text': text}, file)

def json_open(json_file_path):
    with open(json_file_path, "r") as file_1:
        data = json.load(file_1)
        new_content = json.dumps(data)
        return new_content
        