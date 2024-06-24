import os

def directorize(base_path, structure):
    
    for dir_name, subdirs in structure.items():
        dir_path = os.path.join(base_path, dir_name)
        os.makedirs(dir_path, exist_ok = True)
        
        for subdir in subdirs:
            subdir_path = os.path.join(dir_path, subdir)
            os.makedirs(subdir_path, exist_ok = True)
