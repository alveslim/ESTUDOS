from pathlib import Path

root_dir = Path('dados')
file_pats = root_dir.iterdir()
#print(list(file_pats))
for path in file_pats:
    print(path)