from wall import*

import random

class brick():
	def __init__(self,row,col,state):
		self.row=row
		self.col=col
		self.state=state

for i in range(17):
	n1 = random.randint(0,1000)%42
	n2 = random.randint(0,1000)%84
	if n1>1 and n1 < 40:
		if n1%4 ==0 and n2%8>3:
			board1.a[n1][n2-n2%4]= '/'
			board1.a[n1][n2-n2%4+1]='/'
			board1.a[n1][n2-n2%4+2]='/'
			board1.a[n1][n2-n2%4+3]='/'
			board1.a[n1+1][n2-n2%4]='/'
			board1.a[n1+1][n2-n2%4+1]='/'
			board1.a[n1+1][n2-n2%4+2]='/'
			board1.a[n1+1][n2-n2%4+3]='/'
		elif n1%4==1 and n2%8>3:
			board1.a[n1][n2-n2%4]='/'	
			board1.a[n1][n2-n2%4+1]='/'
			board1.a[n1][n2-n2%4+2]='/'
			board1.a[n1][n2-n2%4+3]='/'
			board1.a[n1-1][n2-n2%4]='/'
			board1.a[n1-1][n2-n2%4+1]='/'
			board1.a[n1-1][n2-n2%4+2]='/'
			board1.a[n1-1][n2-n2%4+3]='/'
		elif n1%4 ==2:
			if n2>3 and n2<80:
				board1.a[n1][n2-n2%4]='/'
				board1.a[n1][n2-n2%4+1]='/'
				board1.a[n1][n2-n2%4+2]='/'
				board1.a[n1][n2-n2%4+3]='/'
				board1.a[n1+1][n2-n2%4]='/'
				board1.a[n1+1][n2-n2%4+1]='/'
				board1.a[n1+1][n2-n2%4+2]='/'
				board1.a[n1+1][n2-n2%4+3]='/'
		elif n1%4 ==3:
			if n2>3 and n2<80:
				board1.a[n1][n2-n2%4]='/'
				board1.a[n1][n2-n2%4+1]='/'
				board1.a[n1][n2-n2%4+2]='/'
				board1.a[n1][n2-n2%4+3]='/'
				board1.a[n1-1][n2-n2%4]='/'
				board1.a[n1-1][n2-n2%4+1]='/'
				board1.a[n1-1][n2-n2%4+2]='/'
				board1.a[n1-1][n2-n2%4+3]='/'


			
'''for i in range(42):
	for j in range(84):
		print(board1.a[i][j], end='')
	print(end='\n')'''
