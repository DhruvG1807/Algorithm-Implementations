from collections import deque
from dis import dis

class MazeSolver:
    def __init__(self,matrix):
        self.matrix = matrix
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_dist = -1

    def checkValid(self,x,y):
        if (x>=len(self.matrix) or x<0) or (y<0 or y>= len(self.matrix)):
            return False
        
        elif self.visited[x][y]:
            return False
        
        elif self.matrix[x][y] == 0:
            return False

        else:
            return True
    
    def search(self):
        dest = len(self.matrix)-1
        self.visited[0][0] = True
        q = deque()
        q.append((0,0,0))

        while q:
            (i,j,dist) = q.popleft()

            if i==dest and j == dest:
                self.min_dist = dist
                break

            for move in range(len(self.move_y)):
                next_x = i+self.move_x[move]
                next_y = j+self.move_y[move]

                if self.checkValid(next_x,next_y):
                    self.visited[next_x][next_y] = True
                    q.append((next_x,next_y,dist+1))
    
    def show_result(self):
        if self.min_dist != -1:
            print("The shortest path from source to destination: ", self.min_dist)
        else:
            print("No feasible solution - the destination can not be reached!")



if __name__ == '__main__':

    m = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]

    maze_solver = MazeSolver(m)
    maze_solver.search()
    maze_solver.show_result()

