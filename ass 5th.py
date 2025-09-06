from abc import ABC, abstractmethod

# Abstract base class
class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

# Concrete class for handling text files
class TextFileHandler(FileHandler):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(data)

# Concrete class for handling binary files
class BinaryFileHandler(FileHandler):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data)


text_handler = TextFileHandler('example.txt')
text_handler.write('Hello, world!')
print(text_handler.read())

binary_handler = BinaryFileHandler('example.bin')
binary_handler.write(b'\x00\xFF\x00\xFF')
print(binary_handler.read())
