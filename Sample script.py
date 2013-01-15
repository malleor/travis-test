from glob import glob
from os import cwd
from os.path import join, split, splitext
from frames import execute

MANIFEST = {
  'author': 'John Doe', 
  'version': '0.6',
  'multithreaded': False
}

cloud_extension = IN_PARAMS['cloud_extension']
cloud_ids = []

for path in glob(join(cwd(), '*.'+cloud_extension)):
  name = split(splitext(path)[0])[-1]
  cloud_id = execute('import_cloud', path, name)
  cloud_ids.append(cloud_id)
  
OUT_PARAMS['cloud_ids'] = cloud_ids

# - The whole script is an undivisible unit and is exposed to
#   the framework as a single algorithm.
# - The manifest and input/output params are stored globally. 