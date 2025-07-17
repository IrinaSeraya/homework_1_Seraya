template = {
    "tag": "div",
    "attrs": {"class": "container"},
    "children": [
        {"tag": "h1", "content": "{{ title }}"},
        {"tag": "p", "content": "{{ description }}"},
        {
            "tag": "ul",
            "children": [
                {"tag": "li", "content": "{{ item1 }}"},
                {"tag": "li", "content": "{{ item2 }}"},
            ],
        },
    ],
}

context = {
    "title": "Children",
    "description": "Children under 14",
    "item1": "Anna",
    "item2": "Helen",
}


def render_template(templ, cont):
    new_template = dict()

    def replace_value(a):
        start = a.find("{{ ")
        end = a.find(" }}") + 3
        b = start + 3
        c = end - 3
        context_key = a[b:c]
        a = a[:start] + cont[context_key] + a[end:]
        if ("{{ " and " }}") in a:
            a = replace_value(a)
        return a

    for key, value in templ.items():
        if isinstance(value, str):
            if ("{{ " and " }}") in value:
                value = replace_value(value)
        elif isinstance(value, dict):
            value = render_template(value, cont)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                item = render_template(item, cont)
                value[i] = item
        new_template[key] = value

    return new_template


print(render_template(template, context))