def convert_keys_to_camel_case(data):
    if not isinstance(data, dict):
        return data

    new_data = {}
    for key, value in data.items():
        new_key = to_camel_case(key)
        if isinstance(value, dict):
            new_data[new_key] = convert_keys_to_camel_case(value)
        elif isinstance(value, list):
            new_data[new_key] = [convert_keys_to_camel_case(item) if isinstance(item, dict) else item for item in value]
        else:
            new_data[new_key] = value
    return new_data


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

my_dict = {
    "first_name": "John",
    "last_name": "Doe",
    "address": {
        "street_name": "Main St",
        "house_number": 123
    },
    "phone_numbers": [
        {"number_type": "home", "number": "555-1234"},
        {"number_type": "work", "number": "555-5678"}
    ]
}

camel_case_dict = convert_keys_to_camel_case(my_dict)
print(camel_case_dict)