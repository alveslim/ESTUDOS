from pathlib import Path

root_dir = Path('dados')
file_pats = root_dir.iterdir()
#print(list(file_pats))
for path in file_pats:
    #print(path)
    #print(path.stem)
    #print(path.suffix)
    new_filename = f'new-{path.stem}{path.suffix}'
    #print(new_filename)
    new_filepath = path.with_name(new_filename)
    #print(new_filepath)
    path.rename(new_filepath)