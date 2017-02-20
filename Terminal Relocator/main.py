import sys
from the_copy import Copy
from the_move import Move
from the_cut import Cut
from the_paste import Paste


class Main:

    def __init__(self):
        self.command = None
        self.des_path = None
        self.file_name = None
        self.getCopy = None
        self.getMove = None
        self.getCut = None
        self.getPaste = None

    def main(self):

        if len(sys.argv) < 2:
            raise ValueError("Specify a command and a file!")
        self.command = sys.argv[1].lower()
        if self.command not in ('cut', 'paste'):
            if len(sys.argv) < 3:
                raise ValueError("%s requires a destination path!" % self.command)
            else:
                self.des_path = sys.argv[3]
        if self.command != 'paste':
            self.file_name = sys.argv[2]
        if self.command == 'copy':
            self.getCopy = Copy()
            self.getCopy.copy(self.file_name, self.des_path)
        elif self.command == 'move':
            self.getMove = Move()
            self.getMove.move(self.file_name, self.des_path)
        elif self.command == 'cut':
            self.getCut = Cut()
            self.getCut.cut(self.file_name)
        elif self.command == 'paste':
            self.getPaste = Paste()
            self.getPaste.paste()
        else:
            raise ValueError("Invalid command")

if __name__ == '__main__':
    main()