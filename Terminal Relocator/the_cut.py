import os
import pickle


class Cut:

    def __init__(self):
        self.src_path = None
        self.file_name = None
        self.temp_file = None

    def cut(self, file_name):
        self.src_path = os.path.join(os.getcwd(), file_name)
        self.temp_file = os.path.join(os.getenv('HOMEPATH'), '.tmp')
        pickle.dump(self.src_path, open(self.temp_file, 'wb'))


