from __future__ import annotations

import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_12_input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

class Point:
    plant_type: str
    x: int
    y: int
    perimeter: int
    region: "Region" | None

    def __init__(self, plant_type: str, x: int, y: int) -> None:
        self.plant_type = plant_type
        self.x = x
        self.y = y
        self.perimeter = 4
        self.region = None

class Region:
    points: list[Point]

    def __init__(self) -> None:
        self.points = []

    @property
    def area(self) -> int:
        return len(self.points)

    @property
    def perimeter(self) -> int:
        return sum(point.perimeter for point in self.points)

    @property
    def fence_price(self) -> int:
        return self.area * self.perimeter
    
    def add_point(self, point: Point) -> None:
        point.region = self
        self.points.append(point)
    
    def recurse(self, current_point: Point, matrix: list[list[Point]]) -> None:
        self.add_point(current_point)
        i, j = current_point.y, current_point.x
        north_point = matrix[i - 1][j] if i > 0 else None
        east_point = matrix[i][j + 1] if j < len(matrix[i]) - 1 else None
        south_point = matrix[i + 1][j] if i < len(matrix) - 1 else None
        west_point = matrix[i][j - 1] if j > 0 else None
        test_points = [north_point, east_point, south_point, west_point]
        for test_point in test_points:
            if not test_point:
                continue
            if current_point.plant_type == test_point.plant_type:
                current_point.perimeter -= 1
                if test_point.region is None:
                    self.recurse(test_point, matrix)

matrix = [[Point(plant_type, x, y) for x, plant_type in enumerate(line)] for y, line in enumerate(lines)]
regions: list[Region] = []
for i in range(len(matrix)):
    line = matrix[i]
    for j in range(len(line)):
        point = line[j]
        if not point.region:
            region = Region()
            region.recurse(point, matrix)
            regions.append(region)
print(sum(region.fence_price for region in regions))
# Answer: 1,449,902 - Correct