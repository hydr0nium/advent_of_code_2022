
from typing import *
import re
from treelib import Node, Tree

class DirectoryOrFile():

    def __init__(self):
        self._parent = None
        self._size = 0
        self._subdirectories: List['DirectoryOrFile'] = []
        self._isFolderState = False
        self._name = ""

    def add_file(self, file: 'DirectoryOrFile'):
        self._subdirectories.append(file)
    
    def set_parent(self, folder: 'DirectoryOrFile'):
        self._parent = folder

    def get_parent(self) -> 'DirectoryOrFile':
        return self._parent

    def set_folder_status(self, state: bool):
        self._isFolderState = state

    def set_name(self, name: str):
        self._name = name

    def set_size(self, size: int):
        self._size = size
    
    def get_size(self) -> int:
        return self._size

    def get_children(self) -> List['DirectoryOrFile']:
        return self._subdirectories

    def get_name(self) -> str:
        return self._name

    def isFolder(self):
        return self._isFolderState

    def get_child_by_name(self, name: str) -> 'DirectoryOrFile':
        if(name == ".."):
                return self.get_parent()
        for child in self._subdirectories:
            if(child.get_name()==name):
                return child
        raise LookupError("For " + name + " no child was found in the directory " + self._name)
    
    def __str__(self) -> str:
        return f'''
                Name: {self._name}
                Is Folder?: {self._isFolderState}
                Parent: {self._parent.get_name() if self._parent is not None else None}
                Children: {[x.get_name() for x in self.get_children()]}
                Size: {self.get_size()}
                '''
    def set_size_all(self) -> int:
        size = 0
        if not self.isFolder():
            return self.get_size()
        for child in self.get_children():
            if not child.isFolder:
                size += child.get_size()
                continue
            size += child.set_size_all()
        self.set_size(size)
        return size

    def get_sizes_children(self) -> List[int]:
        return [x.get_size() for x in self.get_children()]
        


def main():
    with open("./input.txt") as f:
        root = DirectoryOrFile()
        root.set_name("/")
        root.set_folder_status(True)
        read_filesystem(f, root)
        needed_space = 30_000_000-(70_000_000-root.get_size())
        print_filesystem(root)
        print(solve_challenge_1(root))
        print(solve_challenge_2(root, needed_space))
                

def read_filesystem(f, root):
    working_directory = root
    cd_pattern = re.compile(r"\$ cd (.+)")
    f.readline()
    line = f.readline()
    while True:
        # If EOF is reached
        if not line:
            break

        # If the command is cd then change the working directory
        if line.startswith("$ cd"):
            working_directory = change_directory(working_directory, line, cd_pattern)
        if line.startswith("$ ls"):
            ls_list, next_line = list_folder(f, working_directory)
            for file_dir in ls_list:
                working_directory.add_file(file_dir)
            line = next_line
            continue

        line = f.readline()
    root.set_size_all()

def solve_challenge_1(directory: DirectoryOrFile) -> int:
    sum = 0
    if not directory.isFolder():
        return sum
    if directory.get_size()<=100000:
        sum += directory.get_size()
    for child in directory.get_children():
        sum += solve_challenge_1(child)
    return sum

def solve_challenge_2(directory: DirectoryOrFile, needed_space: int) -> int:

    if directory.isFolder() and all([not(child.isFolder()) for child in directory.get_children()]):
        return directory.get_size()
    min = directory.get_size()
    for child in directory.get_children():
        if not child.isFolder():
            continue
        candidate_min = solve_challenge_2(child, needed_space)
        if candidate_min < min and candidate_min >= needed_space:
            min = candidate_min
    return min



def change_directory(working_directory: DirectoryOrFile, line: str, pattern) -> DirectoryOrFile:
    folder_name = re.match(pattern, line).group(1)
    folder = working_directory.get_child_by_name(folder_name)
    return folder

def list_folder(file: TextIO, working_directory) -> Tuple[list, str]:
    ls_list = []
    while True:
        line = file.readline()
        if not line:
            return ls_list, line
        elif line.startswith("$"):
            return ls_list, line
        elif line.startswith("dir"):
            dir_name = remove_backslash_n(line.split(" ")[1])
            dir = DirectoryOrFile()
            dir.set_name(dir_name)
            dir.set_folder_status(True)
            dir.set_parent(working_directory)
            ls_list.append(dir)
        else:
            size, file_name = line.split(" ")
            file_name = remove_backslash_n(file_name)
            size = int(remove_backslash_n(size))
            dir = DirectoryOrFile()
            dir.set_name(file_name)
            dir.set_size(size)
            dir.set_parent(working_directory)
            ls_list.append(dir)
            
        
# This is just because I would like to see the whole filesystem printed
def print_filesystem(root: DirectoryOrFile,depth=0):
    tree = Tree()
    createTree(tree, root)
    tree.show()
        
def createTree(t:Tree, root: DirectoryOrFile, parent: DirectoryOrFile=None,counter=0, parentid=0) -> int:
    if parent==None:
        t.create_node(root.get_name(), "0")
    else:
        t.create_node(root.get_name(), str(counter), parent=str(parentid))
    
    parentid = counter
    for child in root.get_children():
        counter += 1
        counter = createTree(t, child, parent=root, counter=counter,parentid=parentid)
    return counter


def process(line: str):
    pass

def remove_backslash_n(string: str):
    return string.strip("\n")

if __name__ == "__main__":
    main()
