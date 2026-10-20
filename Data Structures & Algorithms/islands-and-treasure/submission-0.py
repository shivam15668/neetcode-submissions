class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 :
                    queue.append((r,c))
        
        directions = [(1,0), (0,1), (0,-1), (-1,0)]\

        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr,nc = dr+r, dc+ c

                if not (0<= nr < rows and 0<= nc < cols):
                    continue
                
                if grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c]+1

                queue.append((nr,nc))


