import shutil
import os

class Move:
    def __init__(self):
        self.src_dir = None
        self.dst_dir = None
        self.src_path = None
        self.dst_path = None
        self.file_name = None
    def move(self):
        self.file_name = input('What is the name of the file.\n')
        print('Type the full directory of the file')
        self.src_path = input()
        self.src_dir = os.path.join(self.src_path, self.file_name )
        print('Type the full directory of the destination')
        self.dst_path = input()
        self.dst_dir = os.path.join(self.dst_path, self.file_name)
        shutil.move(self.src_dir, self.dst_dir)


getMove = Move()
getMove.move()
