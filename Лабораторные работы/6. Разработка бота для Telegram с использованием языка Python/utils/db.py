import json


def write_data(data, title="data/data"):
    with open(f"{title}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def load_data(title="data/data"):
    with open(f"{title}.json", "r") as file:
        data = json.load(file)

    return data