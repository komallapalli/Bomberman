import os
class board():

	def __init__(self,width,height):
		self.width=width
		self.height=height
		self.a = [[' 'for i in range(self.width)]for j in range(self.height)]

board1=board(84,42)

for i in range(42):
	if i==0 or i==1 or i==40 or i==41:
		for j in range(84):
			board1.a[i][j]='X'
#print("#",end='')
	else:
		if i%4==1 or i%4==0:
			for j in range(84):
				if j%8 < 4:
					board1.a[i][j]='X'
#					print("#",end='')
				else:
					board1.a[i][j]=' '
#print(" ",end='')
		else:
			for j in range(84):
				if j<4 or j>79:
					board1.a[i][j]='X'
#					print("#",end='')
				else:
					board1.a[i][j]=' '
#					print(" ",end='')
	print(end='\n')		
def printbox():
	os.system('clear')
	for i in range(42): 
		for j in range(84): 
			print(board1.a[i][j],end='')
		print(end='\n') 

