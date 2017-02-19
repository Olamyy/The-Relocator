import shutil
import os

class Paste:
    def __init__(self):
        self.temp = None
        self.dst_dir = None
        self.file_name = None
        self.dst_path = None

    def paste(self):
        self.file_name = input('What is the name of the file you want to paste?\n')
        self.temp = os.path.join(os.getenv('HOMEPATH'), '.tmp')
        self.dst_path = input('Type the full directory of the desired file destination\n')
        self.dst_dir = os.path.join(self.dst_path, self.file_name)
        shutil.move(self.temp, self.dst_dir)


getPaste = Paste()
getPaste.paste()

