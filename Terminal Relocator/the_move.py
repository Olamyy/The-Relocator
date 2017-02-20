import shutil
import os


class Move:

    def __init__(self):
        self.src_path = None
        self.dst_dir = None
        self.file_name = None
        self.dst_path = None

    def move(self,file_name,dst_dir):
		self.src_path = os.path.join(os.getcwd(), file_name)
		self.dst_path = os.path.join(dst_dir, file_name)
		shutil.move(self.src_path, self.dst_path)


