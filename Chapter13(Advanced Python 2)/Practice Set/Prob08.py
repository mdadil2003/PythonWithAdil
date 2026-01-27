# using the DFS (Depth First Search) "Sinking" strategy. This is the most popular way to solve it in interviews because it is clean and efficient.

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r, c):
            # 1. Base Case: Check bounds (if we go off the grid)
            # OR if the current cell is '0' (water), stop.
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            # 2. Sink the Island: Mark current land ('1') as water ('0')
            # so we don't count it again.
            grid[r][c] = '0'

            # 3. Recursive Steps: Visit all 4 neighbors (Up, Down, Left, Right)
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # 4. Iterate through every single cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find land ('1'), it's a NEW island
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c) # Trigger DFS to sink the WHOLE island

        return island_count
