"""
Maze Escape Game  (PS No. 38)
Language : Python 3
Concepts : 2D Lists, Algorithms (BFS), Movement

Legend: # wall, . path, P player, E exit
"""

from collections import deque

# 5x5 maze stored as a 2D list (list of lists)
MAZE = [
    list("P..##"),
    list("##.##"),
    list("#...#"),
    list("#.###"),
    list("#...E"),
]

START = (0, 0)
EXIT = (4, 4)

# W/A/S/D -> (row change, column change)
MOVES = {
    "W": (-1, 0),
    "A": (0, -1),
    "S": (1, 0),
    "D": (0, 1),
}


def print_maze(maze, player):
    """Print the maze with the player's current position shown as P."""
    for r, row in enumerate(maze):
        line = ""
        for c, cell in enumerate(row):
            if (r, c) == player:
                line += "P"
            elif cell == "P":
                line += "."          # start cell becomes a normal path once player leaves
            else:
                line += cell
        print(line)
    print()


def try_move(maze, player, key):
    """
    Try to move the player with a W/A/S/D key.
    Returns (new_position, moved, message).
    Moves into walls or outside the maze are blocked and not counted.
    """
    key = key.upper()
    if key not in MOVES:
        return player, False, f"Invalid key '{key}'. Use W, A, S or D only."

    dr, dc = MOVES[key]
    nr, nc = player[0] + dr, player[1] + dc

    if nr < 0 or nr >= len(maze) or nc < 0 or nc >= len(maze[0]):
        return player, False, f"Cannot move outside the maze. Player stays at {player}"

    if maze[nr][nc] == "#":
        return player, False, f"Wall ahead. Move blocked. Player stays at {player}"

    return (nr, nc), True, f"Player moved to (row{nr}, col{nc})"


def shortest_path(maze, start, goal):
    """BFS: returns the shortest path (list of cells) from start to goal, or None."""
    queue = deque([start])
    parent = {start: None}

    while queue:
        cur = queue.popleft()
        if cur == goal:
            path = []
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return path[::-1]
        for dr, dc in MOVES.values():
            nr, nc = cur[0] + dr, cur[1] + dc
            if (0 <= nr < len(maze) and 0 <= nc < len(maze[0])
                    and maze[nr][nc] != "#" and (nr, nc) not in parent):
                parent[(nr, nc)] = cur
                queue.append((nr, nc))
    return None


def play(maze=MAZE):
    """Interactive game loop."""
    player = START
    total_moves = 0
    print("Use W (up), A (left), S (down), D (right). Type Q to quit.\n")
    print_maze(maze, player)

    while player != EXIT:
        key = input("Move: ").strip()
        if key.upper() == "Q":
            print("Game ended.")
            return
        if not key:
            continue
        player, moved, message = try_move(maze, player, key[0])
        if moved:
            total_moves += 1
        print(message)
        print_maze(maze, player)
        print(f"Moves: {total_moves}\n")

    print(f"You escaped the maze! Total moves: {total_moves}")


def show_shortest(maze=MAZE):
    path = shortest_path(maze, START, EXIT)
    if path is None:
        print("No path exists from start to exit.")
        return
    print("Shortest path (row, col):")
    print(" -> ".join(str(p) for p in path))
    print(f"Shortest path length: {len(path) - 1} steps")


def main():
    while True:
        print("===== MAZE ESCAPE GAME =====")
        print("1. Play game")
        print("2. Shortest path (BFS)")
        print("3. Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            play()
        elif choice == "2":
            show_shortest()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1, 2 or 3.")
        print()


if __name__ == "__main__":
    main()
