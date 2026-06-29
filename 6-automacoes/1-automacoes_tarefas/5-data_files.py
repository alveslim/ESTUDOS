from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob('**/*'):
    if path.is_file():
        
        
        # data & hora
        stats = path.stat()
        second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(second_created)
        #print(f"Date created: {date_created}")
        date_modified = date_created.strftime('%Y-%m-%d_%H:%M:%S')
        #print(f"Date modified: {date_modified}")
        
        # nome:
        new_filename = f"{date_modified}-{path.name}"
        #print(new_filename)
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)