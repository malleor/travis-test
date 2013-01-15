from glob import glob
from os import cwd
from os.path import join, split, splitext
from frames import execute

MANIFEST = {
  'doc': 'Loads all clouds of given format from the CWD.',
  'author': 'John Doe', 
  'version': '0.6',
  'multithreaded': False
}
DEF_IN_PARAMS['cloud_extension'] = 'copsxml'
cloud_extension = IN_PARAMS['cloud_extension']

if __name__ == '__main__':
  cloud_ids = []
  
  for path in glob(join(cwd(), '*.'+cloud_extension)):
    name = split(splitext(path)[0])[-1]
    cloud_id = execute('import_cloud', path, name)
    cloud_ids.append(cloud_id)
  
  OUT_PARAMS['cloud_ids'] = cloud_ids


# - The whole script is an undivisible unit and is exposed to
#   the framework as a single algorithm.
# - The manifest and input/output params are stored globally. 