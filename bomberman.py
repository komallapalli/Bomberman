from bricks import*

from wall import*

from getchunix import*

from person import*

import time

getch = GetchUnix()

class bomp(person):
	def __init__(self,row,col,score,lives):
		person.__init__(self,row,col)
		self.lives=lives
		self.score=score
	def rowcor(self):
		return self.row
	def colcor(self):
		return self.col
	def point(self):
		self.score=self.score+20
	def update_up_down(self,k):
		self.row=self.row+k
	def update_side(self,k):
		self.col=self.col+k
	def up(self):
		if board1.a[self.rowcor()-1][self.colcor()]==' ':
			for i in range(1,3):
				for j in range(4):
					board1.a[self.rowcor()-i][self.colcor()+j]='B'
			for i in range(0,2):
				for j in range(4):
					if board1.a[self.rowcor()][self.colcor()]=='O':
						board1.a[self.rowcor()+i][self.colcor()+j]='O'
					else:
						board1.a[self.rowcor()+i][self.colcor()+j]=' '
			self.update_up_down(-2)
	
	def down(self):
		if board1.a[self.rowcor()+2][self.colcor()]==' ':
			for i in range(2,4):
				for j in range(4):
					board1.a[self.rowcor()+i][self.colcor()+j]='B'
			for i in range(0,2):
				for j in range(4):
					if board1.a[self.rowcor()][self.colcor()]=='O':
						board1.a[self.rowcor()+i][self.colcor()+j]='O'
					else:
						board1.a[self.rowcor()+i][self.colcor()+j]=' '
			self.update_up_down(2)
	
	def right(self):
		if board1.a[self.rowcor()][self.colcor()+4]==' ':
			for i in range(2):
				for j in range(4,8):
					board1.a[self.rowcor()+i][self.colcor()+j]='B'
			for i in range(2):
				for j in range(0,4):
					if board1.a[self.rowcor()][self.colcor()]=='O':
						board1.a[self.rowcor()+i][self.colcor()+j]='O'
					else:
						board1.a[self.rowcor()+i][self.colcor()+j]=' '
			self.update_side(4)
	
	def left(self):
		if board1.a[self.rowcor()][self.colcor()-1]==' ':
			for i in range(2):
				for j in range(1,5):
					board1.a[self.rowcor()+i][self.colcor()-j]='B'
			for i in range(2):
				for j in range(0,4):
					if board1.a[self.rowcor()][self.colcor()]=='O':
						board1.a[self.rowcor()+i][self.colcor()+j]='O'
					else:
						board1.a[self.rowcor()+i][self.colcor()+j]=' '
			self.update_side(-4)
	

bomp=bomp(2,4,0,3)
for i in range(2,4):
	for j in range(4,8):
		board1.a[i][j]='B'
printbox()
var1=100000000000
var2=0
flag=0
xinit=0
yinit=0
while True:
	var2=time.time()
	income=getch()
	if income == 'q':
		exit()
	if income == 'w':
		bomp.up()
	if income == 's':
		bomp.down()
	if income == 'a':
		bomp.left()
	if income == 'd':
		bomp.right()
	if income == 'b':
		xinit=bomp.rowcor()
		yinit=bomp.colcor()
		for i in range(2):
			for j in range(4):
				board1.a[bomp.rowcor()+i][bomp.colcor()+j]='O'
		var1=time.time()
	printbox()
#	print(var2-var1)
#	print(xinit,yinit)
	if var2-var1>3 and flag==0:
		for i in range(2):
			for j in range(4):
				board1.a[xinit+i][yinit+j]='e'
		if board1.a[xinit][yinit+4]=='/':
			for i in range(2):
				for j in range(4,8):
					board1.a[xinit+i][yinit+j]=' '
		if board1.a[xinit][yinit-1]=='%':
			for i in range(2):
				for j in range(1,5):
					board1.a[xinit+i][yinit-j]=' '
		if board1.a[xinit-1][yinit]=='%':
			for i in range(1,3):
				for j in range(4):
					board1.a[xinit-i][yinit+j]=' '
		if board1.a[xinit+2][yinit]=='%':
			for i in range(2,4):
				for j in range(4):
					board1.a[xinit+i][yinit+j]=' '    

		flag=1
	if flag:
		flag+=1
	if flag == 3:
		for i in range(2):
			for j in range(4):
				board1.a[xinit+i][yinit+j]=' '
		flag=0
#	printbox()
