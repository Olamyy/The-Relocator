import shutil
import os

class Copy:
    def __init__(self):
        self.src_dir = None
        self.temp = None
        self.file_name = None
        self.src_path = None

    def copy(self):
        print('Type the full directory of the file.')
        self.src_path = input()
        self.file_name = input('What is the name of the file you want to copy?\n')
        self.src_dir = os.path.join(self.src_path, self.file_name)
        self.temp = os.path.join(os.getenv('HOMEPATH'), '.tmp')
        shutil.copyfile(self.src_dir, self.temp)




getCopy = Copy()
getCopy.copy()


