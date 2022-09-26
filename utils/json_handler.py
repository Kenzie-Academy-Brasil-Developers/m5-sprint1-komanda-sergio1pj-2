import json


def read_json(filepath: str) -> list[dict]:
    try:
        with open(filepath, 'r', encoding="utf8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []
def write_json(filepath: str, data: list[dict]) -> list[dict]:
    read = read_json(filepath)
    id = read[-1]["id"] + 1 if len(read) > 0 else 1
    data["id"] = id
    read.append(data)
    with open(filepath, 'w') as file:
        json.dump(read, file, indent=4)
    return data  
