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

    def empty(self):
        return all([i == "." for i in self.arr])

class FreeSpace(Block):
    def __init__(self, n: int):
        self.arr = ["." for _ in range(n)]
    
    def free(self):
        return any([i == "." for i in self.arr])

class Disk:
    blocks: list[Block]

    def __init__(self):
        self.blocks = []

    def __str__(self):
        s = ""
        for block in self.blocks:
            for value in block.arr:
                s += str(value)
        return s

    def add_block(self, block: Block):
        self.blocks.append(block)
    
    def get_last_file(self):
        for block in reversed(self.blocks):
            if isinstance(block, File):
                if not block.empty():
                    return block
    
    def get_first_free_space(self):
        for block in self.blocks:
            if isinstance(block, FreeSpace):
                if block.free():
                    return block
    
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
    
    def compacted(self):
        dot_found = False
        for block in self.blocks:
            for value in block.arr:
                if value == ".":
                    dot_found = True
                if dot_found and value != ".":
                    return False
        return True
    
    def compact(self):
        while not self.compacted():
            last_file = self.get_last_file()
            first_free_space = self.get_first_free_space()
            self.transfer(last_file, first_free_space)

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
# Answer: 6,359,213,660,505 - Correct