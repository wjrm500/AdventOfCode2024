import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_9_input.txt") as f:
    text = f.read()

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class Block:
    arr: list[str]

class File(Block):
    def __init__(self, n: int, id_number: int):
        self.arr = [str(id_number) for _ in range(n)]
        self.move_attempted = False

class FreeSpace(Block):
    def __init__(self, n: int):
        self.arr = ["." for _ in range(n)]
    
    def can_fit(self, file: File):
        return self.arr.count(".") >= len(file.arr)

class Disk:
    blocks: list[Block]
    files: list[File]
    free_spaces: list[FreeSpace]

    def __init__(self):
        self.blocks = []
        self.files = []
        self.free_spaces = []

    def __str__(self):
        s = ""
        for block in self.blocks:
            for value in block.arr:
                s += str(value)
        return s

    def add_block(self, block: Block):
        self.blocks.append(block)
        if isinstance(block, File):
            self.files.append(block)
        if isinstance(block, FreeSpace):
            self.free_spaces.append(block)
    
    def get_last_file(self):
        for file in reversed(self.files):
            if not file.move_attempted:
                return file
    
    def transfer(self, file: File, free_space: FreeSpace):
        for i, value in enumerate(file.arr):
            if value == ".":
                i = i - 1
                break
        else:
            i = -1
        num_to_transfer = file.arr[i]
        file.arr[i] = "."
        idx_to_transfer_into = free_space.arr.index(".")
        free_space.arr[idx_to_transfer_into] = num_to_transfer
    
    def attempt_move(self, file: File):
        file.move_attempted = True
        for free_space in self.free_spaces:
            if free_space.can_fit(file):
                for _ in range(len(file.arr)):
                    self.transfer(file, free_space)
                return

    def compacted(self):
        return all([file.move_attempted for file in self.files])
    
    def compact(self):
        while not self.compacted():
            last_file = self.get_last_file()
            self.attempt_move(last_file)

    def checksum(self):
        values = [value for block in self.blocks for value in block.arr]
        return sum([i * int(value) for i, value in enumerate(values) if value != "."])

disk = Disk()
for i, chunk in enumerate(chunks(text, 2)):
    chunk = [int(num) for num in chunk]
    file_n = chunk[0]
    file = File(file_n, i)
    disk.add_block(file)
    if len(chunk) == 2:
        free_space_n = chunk[1]
        free_space = FreeSpace(free_space_n)
        disk.add_block(free_space)

disk.compact()
print(disk.checksum())
print(disk)
# Answer: 8,583,576,817,788 - Incorrect