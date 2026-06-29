from pathlib import Path

root_dir = Path('files')
# file_paths = root_dir.iterdir()
# for path in file_paths:
#         print(path)
#         for filepath in path.iterdir():
#             print(filepath)
file_paths = root_dir.glob('**/*') # ** ta referindo aos diretorios que venha ter 
# e /* para fazer a leitura de todos os arquivos dentro desses diretorios
for path in file_paths:
    #print(path)
    if path.is_file(): #  
        #print(path)
        parent_folder = path.parts[-2]
        new_filename = f"{parent_folder}-{path.name}"
        #print(new_filename)
        new_filepath = path.with_name(new_filename)
        #print(new_filepath)
        path.rename(new_filepath) 
        
        """
        antes: 
        dados\folder1\file1.txt
        depois:
        dados\folder1\folder1-file1.txt
        """
        