from contextlib import contextmanager


with open('sample.txt', 'r') as f:
    for line in f.readlines():
        print(line)


class ManagedFile:

    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.file = open(self.name, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile("sample.txt") as f:
    for line in f.readlines():
        print(line)

@contextmanager
def managed_file2(name):
    try:
        f = open(name,'r')
        yield f
    finally:
        f.close()

class Indenter:

    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
    
    def print(self, text):
        print(' ' * self.level + text)

with Indenter() as indent:
    indent.print("Hello")
    with indent:
        indent.print("There")
        with indent:
            indent.print("Lol wtf")
    print("Back to top")    

