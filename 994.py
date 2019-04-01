class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d=0
        while True:
            c=False
            old=[]
            for i in range(len(grid)):
                s=[]
                for j in range(len(grid[0])):
                    s.append(grid[i][j])
                old.append(s)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if old[i][j]==2:                        
                        f=self.change(grid,i,j)
                        if f:
                            c=True
            if c==False:
                break
            else:
                d=d+1
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        return -1
        return d
    def change(self,grid,i,j):
        r=False
        for ti,tj in zip([-1,0,0,1],[0,-1,1,0]):
            if ti+i>=0 and ti+i<len(grid) and tj+j>=0 and tj+j<len(grid[0]):
                if grid[ti+i][tj+j]==1:
                    grid[ti+i][tj+j]=2
                    r=True
        return r
