import shutil
import os


class Copy:

    def __init__(self):
        self.src_path = None
        self.dst_path = None
        self.file_name = None
        self.dst_dir = None

    def copy(self, file_name, dst_dir):
        self.src_path = os.path.join(os.getcwd(), file_name)
        self.dst_path = os.path.join(dst_dir, file_name)
        shutil.copyfile(self.src_path, self.dst_path)


