# Maze Escape Game (PS No. 38)

A console-based maze game in Python 3. The player moves through a 5x5 maze stored as a 2D list using **W / A / S / D** keys and must reach the exit. The program also finds the shortest path from start to exit using **BFS (Breadth First Search)**.

**Student:** Satyam Kumar Singh
**Project:** Maze Escape Game | **PS No.:** 38
**Concepts:** 2D Lists, Algorithms (BFS), Movement

## Maze

```
P..##
##.##
#...#
#.###
#...E
```

`#` wall, `.` path, `P` start (row 0, col 0), `E` exit (row 4, col 4)

## How to run

```
python3 one.py
```

Menu:
1. **Play game**: move with W/A/S/D (Q to quit). The maze is printed after every move.
2. **Shortest path (BFS)**: prints the shortest route and its length.
3. **Exit**

## Rules
- Moves into walls or outside the maze are blocked and **not counted**.
- Invalid keys show: `Invalid key 'X'. Use W, A, S or D only.`
- On reaching `E`, the game prints `You escaped the maze! Total moves: N`.

## Files
| File | Description |
|------|-------------|
| `one.py` | Main program |
| `README.md` | Project description |
| `Test_cases_passed.pdf` | Output of the 4 test cases |
| `PS38_project_details.jpg` | Project allocation details (PS No. 38) |

No CSV/TXT files are used in this project.

## Test cases
| # | Input | Output |
|---|-------|--------|
| 1 | D | Player moved to (row0, col1) \| Moves: 1 |
| 2 | W at (0,0) | Cannot move outside the maze. Player stays at (0, 0) \| Moves: 0 |
| 3 | D, D, D, X | Wall ahead. Move blocked. Invalid key 'X'. Moves counted: 2 |
| 4 | D,D,S,S,A,S,S,D,D,D | You escaped the maze! Total moves: 10, shortest path length: 10 steps |
