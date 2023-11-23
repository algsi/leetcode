"""
841. keys and rooms

钥匙和房间
"""

from typing import List


class Solution:
    """
    DFS
    """
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()  # the visited rooms
        visited.add(0)

        def visit(room: int):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    # visit the room with the key
                    visit(key)

        visit(0)
        return len(visited) == n


def main():
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    solution = Solution()
    print(solution.canVisitAllRooms(rooms))


if __name__ == '__main__':
    main()
