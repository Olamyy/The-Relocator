import shutil
import os
from core.errors import InvalidPathError,RequiresFileError


class Copy:
    def __init__(self, **kwargs):
        self.src_dir = kwargs.get('copy_dir', None)

    @staticmethod
    def is_valid_path(path):
        if os.path.isdir(path):
            return True
        else:
            return False

    @staticmethod
    def is_valid_file(file_name):
        if os.path.isfile(file_name):
            return True
        else:
            return False

    def copy_file(self):
        if self.is_valid_path(self.src_dir):
            self.copy_dir()
        elif self.is_valid_file(self.src_dir):
            temp = os.path.join('/home/lekanterragon/Desktop/ex_repo-master', '.txt')
            shutil.copyfile(self.src_dir, temp)

    def copy_dir(self):
        if self.is_valid_path(self.src_dir):
            temp = os.path.join(os.getenv('HOME'), '.tmp')
            shutil.copyfile(self.src_dir, temp)
        else:
            self.copy_file()


test = Copy(copy_dir='/home/lekanterragon/Desktop/ex_repo-master/core/my_copy.py')
test.copy_file()



