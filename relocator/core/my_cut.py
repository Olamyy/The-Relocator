import shutil
import os


class Cut:

    def __init__(self):
        self.src_dir = None
        self.temp = None
        self.file_name = None
        self.src_path = None

    def cut(self):
        self.src_path = input('Type in the full directory of the file you want to cut\n')
        self.file_name = input('What is the name of the file?\n')
        self.src_dir = os.path.join(self.src_path, self.file_name)
        self.temp = os.path.join(os.getenv('HOMEPATH'), '.tmp')

        shutil.move(self.src_dir, self.temp)


getCut = Cut()
getCut.cut()

