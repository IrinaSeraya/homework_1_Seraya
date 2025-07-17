def find_files_by_extension(tree, extention, current_path="", result=None):
    if result is None:
        result = []

    for name, content in tree.items():
        new_path = f"{current_path}/{name}" if current_path else name
        if isinstance(content, list):
            for filename in content:
                if filename.endswith(f".{extention}"):
                    result.append(f"{new_path}/{filename}")
        elif isinstance(content, dict):
            find_files_by_extension(content, extention, new_path, result)
    return result

TREE = {
    "documents": {
        "reports": ["report1.txt", "report2.pdf"],
        "presentations": ["pres1.pptx", "pres2.pdf"],
        "misc": ["todo.txt", "image.png"]
    },
    "pictures": ["vacation.jpg", "city.png"],
    "project_a": {
        "src": ["main.py", "utils.py"],
        "data": ["input.csv"]
    }
}

txt_files = find_files_by_extension(TREE, "txt")
print(txt_files)