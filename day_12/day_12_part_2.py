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
    region: "Region" | None
    boundary_edges: set[str]

    def __init__(self, plant_type: str, x: int, y: int) -> None:
        self.plant_type = plant_type
        self.x = x
        self.y = y
        self.region = None
        self.boundary_edges = set()

class Region:
    matrix: list[list[Point]]
    points_traversed: list[Point]

    def __init__(self, matrix: list[list[Point]]) -> None:
        self.matrix = matrix
        self.points_traversed = []

    @property
    def area(self) -> int:
        return len(self.points_traversed)

    @property
    def side_count(self) -> int:
        self.eliminate_collinear_boundary_edges()
        return sum(len(point.boundary_edges) for point in self.points_traversed)

    @property
    def fence_price(self) -> int:
        return self.area * self.side_count
    
    def add_point(self, point: Point) -> None:
        point.region = self
        self.points_traversed.append(point)

    def get_neighbour_point_tuples(self, current_point: Point) -> list[tuple[str, Point]]:
        i, j = current_point.y, current_point.x
        north_point = self.matrix[i - 1][j] if i > 0 else None
        east_point = self.matrix[i][j + 1] if j < len(self.matrix[i]) - 1 else None
        south_point = self.matrix[i + 1][j] if i < len(self.matrix) - 1 else None
        west_point = self.matrix[i][j - 1] if j > 0 else None
        return [("N", north_point), ("E", east_point), ("S", south_point), ("W", west_point)]
    
    def recurse(self, current_point: Point) -> None:
        self.add_point(current_point)
        neighbour_point_tuples = self.get_neighbour_point_tuples(current_point)
        boundary_edges = set()
        for direction, neighbour_point in neighbour_point_tuples:
            if not neighbour_point or current_point.plant_type != neighbour_point.plant_type:
                boundary_edges.add(direction)
            if not neighbour_point:
                continue
            if current_point.plant_type == neighbour_point.plant_type:
                if neighbour_point.region is None:
                    self.recurse(neighbour_point)
        current_point.boundary_edges = boundary_edges
    
    def eliminate_collinear_boundary_edges(self) -> None:
        self.points_traversed = sorted(self.points_traversed, key=lambda p: (p.y, p.x))
        for point in self.points_traversed:
            neighbour_point_tuples = self.get_neighbour_point_tuples(point)
            neighbour_points = [t[1] for t in neighbour_point_tuples]
            neighbour_boundary_edges = set()
            for neighbour_point in neighbour_points:
                if neighbour_point and point.plant_type == neighbour_point.plant_type:
                    neighbour_boundary_edges |= neighbour_point.boundary_edges
            collinear_boundary_edges = point.boundary_edges & neighbour_boundary_edges
            for collinear_boundary_edge in collinear_boundary_edges:
                point.boundary_edges.remove(collinear_boundary_edge)

# Find boundary edges
matrix = [[Point(plant_type, x, y) for x, plant_type in enumerate(line)] for y, line in enumerate(lines)]
regions: list[Region] = []
for i in range(len(matrix)):
    line = matrix[i]
    for j in range(len(line)):
        point = line[j]
        if not point.region:
            region = Region(matrix)
            region.recurse(point)
            regions.append(region)

print(sum(region.fence_price for region in regions))
# Answer: 908,042 - Correct