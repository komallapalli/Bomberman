import random
from person import *
class Enemy(Person):
    def __init__(self,row,col,life):
        Person.__init__(self,row,col)
        self.life=life
    def CreateEnemy(self,board1.a,c1):
        for i in range(4):
            for j in range(2):
                board1.a[self.row+j][self.col+i]=c1
        return board1.a
    def GenerateEnemy(self,board1.a):
        self.CreateEnemy(board1.a,'E')
        return board1.a
    def RandomMove(self,board1.a):
        while True:
            i=random.randint(0,3)
            if i==0 and board1.a[self.row-2][self.col]==' ' :
                self.up(board1.a)
                break
            elif i == 1 and board1.a[self.row+2][self.col]==' ':
                self.down(board1.a)
                break
            elif i is 2 and board1.a[self.row][self.col-4]==' ':
                self.left(board1.a)
                break
            elif i is 3 and board1.a[self.row][self.col+4]==' ':
                self.right(board1.a)
                break
        return board1.a


for i in range(6):
	xax = random.randint(0,1000)%42
	yax = random.randint(0,1000)%84

