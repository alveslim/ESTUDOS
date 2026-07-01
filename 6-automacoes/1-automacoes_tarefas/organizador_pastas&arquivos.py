from pathlib import Path

rootdir = Path("files")

txt_files = rootdir.rglob("*.txt")
destiny_txt = Path('files/txt')
destiny_txt.mkdir(parents=True, exist_ok=True)

for path2 in txt_files:
    if path2.is_file():
        if path2.name != destiny_txt:
            caminho_final = destiny_txt / path2.name # str(destiny_txt) + '/' + path2.name
            path2.rename(caminho_final)
