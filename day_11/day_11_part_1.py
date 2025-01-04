from __future__ import annotations

import os
from typing import Iterator

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_11_input.txt") as f:
    text = f.read()

class Pebble:
    next: "Pebble" | None
    value: int

    def __init__(self, value: int) -> None:
        self.next = None
        self.value = value
    
    def __repr__(self) -> str:
        return str(self.value)
    
    def transform(self) -> "Pebble":
        if self.value == 0:
            self.value = 1
            return self
        elif (num_chars := len((str_val := str(self.value)))) % 2 == 0:
            divider = int(num_chars / 2)
            first_value = int(str_val[:divider])
            second_value = int(str_val[divider:])
            new_pebble = Pebble(first_value)
            new_pebble.next = self.next
            self.next = new_pebble
            self.value = second_value
            return new_pebble
        else:
            self.value *= 2024
            return self

class PebbleChain:
    head: Pebble | None

    def __init__(self) -> None:
        self.head = None
    
    def __len__(self) -> int:
        x = 0
        temp = self.head
        while True:
            if temp is None:
                break
            x += 1
            temp = temp.next
        return x
    
    def __iter__(self) -> Iterator[Pebble]:
        l = []
        temp = self.head
        while True:
            if temp is None:
                break
            l.append(temp)
            temp = temp.next
        l = reversed(l)
        return iter(l)

    def add_pebble(self, pebble: Pebble) -> None:
        pebble.next = self.head
        self.head = pebble
    
    def blink(self) -> None:
        temp = self.head
        while True:
            if temp is None:
                break
            temp = temp.transform()
            temp = temp.next
    
    def blink_x_times(self, x: int) -> None:
        for _ in range(x):
            self.blink()
    
pebble_chain = PebbleChain()
for value in map(int, text.split()):
    pebble = Pebble(value)
    pebble_chain.add_pebble(pebble)

x = 25
PRINT_PEBBLES = 0
if PRINT_PEBBLES:
    print("Initial arrangement:")
    for pebble in iter(pebble_chain):
        print(pebble.value, end=" ")
        print("\n")
    for i in range(x):
        if i + 1 == 3:
            a = 1
        pebble_chain.blink()
        print(f"After {i + 1} blinks:")
        for pebble in iter(pebble_chain):
            print(pebble.value, end=" ")
        print("\n")
else:
    pebble_chain.blink_x_times(x)
print(len(pebble_chain))
# Answer: 231,278 - Correct