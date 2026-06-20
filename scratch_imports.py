import os
import ast
import sys

def get_imports(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        try:
            tree = ast.parse(f.read(), filename=filepath)
        except SyntaxError:
            return set()

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.add(name.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

project_dir = r"c:\Users\asus9\Desktop\Codes\Food_ordering\food_ordering"
all_imports = set()

for root, dirs, files in os.walk(project_dir):
    if 'venv' in root or 'env' in root or '__pycache__' in root or 'staticfiles' in root:
        continue
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            # Skip this script itself
            if 'scratch_imports.py' in filepath:
                continue
            all_imports.update(get_imports(filepath))

print("IMPORTS FOUND:")
for imp in sorted(all_imports):
    print(imp)
