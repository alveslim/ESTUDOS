from pathlib import Path
from datetime import datetime

path = Path('files', 'dados', 'a.txt')
#print(path)
#print(path.stat())
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
#print(f"Date created: {date_created}")
date_modified = date_created.strftime('%Y-%m-%d_%H:%M:%S')
print(f"Date modified: {date_modified}")