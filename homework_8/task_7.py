def serialize(data):
    if isinstance(data, str):
        return '"' + data.replace('\\', '\\\\').replace('"', '\\"') + '"'
    elif isinstance(data, int) or isinstance(data, float):
        return str(data)
    elif isinstance(data, bool):
        return "true" if data else "false"
    elif isinstance(data, list):
        return "[" + ", ".join(serialize(item) for item in data) + "]"
    elif isinstance(data, dict):
        return "{" + ", ".join(f'"{key}":{serialize(value)}' for key, value in data.items()) + "}"
    elif data is None:
        return "null"
    else:
        raise TypeError(f"Unsupported type: {type(data)}")
    
data = {
    "name": "Иван",
    "age": 30,
    "city": "Минск",
    "is_student": False,
    "grades": [85, 92, 78]
}

print(serialize(data))