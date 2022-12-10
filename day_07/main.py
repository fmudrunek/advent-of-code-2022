from __future__ import annotations

from pathlib import Path
from typing import List


class Node:
    def __init__(self, parent: Node, name: str, is_dir: bool = True) -> None:
        self.parent = parent
        self.name = name
        self.children = []
        self.size = 0
        self.is_dir = is_dir

    def calculate_size(self) -> None:
        self.size = sum([child.calculate_size() for child in self.children])
        return self.size


class File(Node):
    def __init__(self, parent: Node, name: str, size: int) -> None:
        super().__init__(parent, name, is_dir=False)
        self.size = size

    def calculate_size(self) -> None:
        return self.size


def _solve_command(command: str, current_node: Node) -> Node:
    if command == "$ ls":
        return current_node
    if command == "$ cd ..":
        return current_node.parent

    target = command[5:]
    return next(child for child in current_node.children if child.name == target)


def _build_tree_structure(root: Node, commands: List[str]) -> None:
    current_node = root

    for line in commands:
        if line == "$ cd /":
            current_node = root
            continue

        if line.startswith("$"):
            current_node = _solve_command(line, current_node)
        else:
            if line.startswith("dir"):
                dir_name = line[4:]
                current_node.children.append(Node(current_node, dir_name))
            else:
                size, name = line.split()
                current_node.children.append(File(current_node, name, int(size)))

    root.calculate_size()


def solve_part_1(data: List[str]) -> int:
    root = Node(None, "/", True)
    _build_tree_structure(root, data)

    small_dicts: List[Node] = []

    def get_small_dicts(node: Node):
        if not node.is_dir:
            return

        for child in [_ for _ in node.children if _.is_dir]:
            if child.size < 100000:
                small_dicts.append(child)
            get_small_dicts(child)

    get_small_dicts(root)
    return sum([node.size for node in small_dicts])


def solve_part_2(data: List[str]) -> int:
    root = Node(None, "/", True)
    _build_tree_structure(root, data)

    unused_space = 70000000 - root.size
    needed = 30000000 - unused_space

    smallest_possible = root.size

    def find_smallest(node: Node):
        nonlocal smallest_possible
        if needed <= node.size < smallest_possible:
            smallest_possible = node.size

        for child in [_ for _ in node.children if _.is_dir]:
            find_smallest(child)

    find_smallest(root)
    return smallest_possible


def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")
