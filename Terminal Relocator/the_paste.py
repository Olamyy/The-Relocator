import shutil
import os
import pickle


class Paste:

    def __init__(self):
        self.src_path = None
        self.file_name = None
        self.temp_file = None
        self.dst_dir = None
        self.dst_path = None

    def paste(self, dst_dir=os.getcwd()):
        self.temp_file = os.path.join(os.getenv('HOMEPATH'), '.tmp')
        self.src_path = pickle.load(open(self.temp_file, 'rb'))
        self.file_name = self.src_path.split(os.path.sep)[-1]
        self.dst_path = os.path.join(dst_dir, self.file_name)
        shutil.move(self.src_path, self.dst_path)


