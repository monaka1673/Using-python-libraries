from pathlib import Path
path = Path()
# print(path)
# print(path.glob('*.py'))
for filepath in path.glob('*.py'):
    print(filepath)