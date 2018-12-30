board = [[0 for x in range(8)]for x in range(8)]
MAX=9
start=()
end=()
came_from={}
cost_so_far={}
open=[]
close=[]
neighbours=[]
n_cost={}
ans=[]

def getNeighbours(current):
	upperLeft(current)
	upperRight(current)
	lowerLeft(current)
	lowerRight(current)

def upperLeft(current):
	if(current[0]-2>=1 and current[0]-2<MAX and current[1]-1>=1 and current[1]-1<MAX):
		neighbours.extend([(current[0]-2,current[1]-1)])
		n_cost[(current[0]-2,current[1]-1)]=calFN((current[0]-2,current[1]-1),current)
	if(current[0]-1>=1 and current[0]-1<MAX and current[1]-2>=1 and current[1]-2<MAX):
		neighbours.extend([(current[0]-1,current[1]-2)])		
		n_cost[(current[0]-1,current[1]-2)]=calFN((current[0]-1,current[1]-2),current) 	
def upperRight(current):
	if(current[0]-2>=1 and current[0]-2<MAX and current[1]+1>=1 and current[1]+1<MAX):
		neighbours.extend([(current[0]-2,current[1]+1)])
		n_cost[(current[0]-2,current[1]+1)]=calFN((current[0]-2,current[1]+1),current)
	if(current[0]-1>=1 and current[0]-1<MAX and current[1]+2>=1 and current[1]+2<MAX):
		neighbours.extend([(current[0]-1,current[1]+2)])	
		n_cost[(current[0]-1,current[1]+2)]=calFN((current[0]-1,current[1]+2),current)	 	
def lowerLeft(current):
	if(current[0]+2>=1 and current[0]+2<MAX and current[1]-1>=1 and current[1]-1<MAX):
		neighbours.extend([(current[0]+2,current[1]-1)])
		n_cost[(current[0]+2,current[1]-1)]=calFN((current[0]+2,current[1]-1),current)
	if(current[0]+1>=1 and current[0]+1<MAX and current[1]-2>=1 and current[1]-2<MAX):
		neighbours.extend([(current[0]+1,current[1]-2)])	
		n_cost[(current[0]+1,current[1]-2)]=calFN((current[0]+1,current[1]-2),current)
def lowerRight(current):
	if(current[0]+2>=1 and current[0]+2<MAX and current[1]+1>=1 and current[1]+1<MAX):
		neighbours.extend([(current[0]+2,current[1]+1)])
		n_cost[(current[0]+2,current[1]+1)]=calFN((current[0]+2,current[1]+1),current)
	if(current[0]+1>=1 and current[0]+1<MAX and current[1]+2>=1 and current[1]+2<MAX):
		neighbours.extend([(current[0]+1,current[1]+2)])		 	
		n_cost[(current[0]+1,current[1]+2)]=calFN((current[0]+1,current[1]+2),current)

def calFN(current,parent):
	return calHN(current)+calGN(parent)

def calHN(current):
	if current==start:
		return 0
	return abs(current[0]-end[0])+abs(current[1]-end[1])

def calGN(parent):
	if parent == (-1,-1):
		return 0
	else:
		return cost_so_far[parent]+1

def solveGame():
	while len(open)>0:

		node=getMinimum()
		close.extend([node])
		if node==end:
			displayAns();
			exit()
		else:
			getNeighbours(node)
			for n in neighbours:
				if n in close and cost_so_far[n]>n_cost[n]:
					close.remove(n)
					open.extend([n])
					came_from[n]=node
					cost_so_far[n]=n_cost[n]
				elif n in open and cost_so_far[n]>n_cost[n]:
					cost_so_far[n]=n_cost[n]
					came_from[n]=node
				elif n not in open and n not in close:
					open.extend([n])
					cost_so_far[n]=n_cost[n]
					came_from[n]=node
			del neighbours[:]
	print "No Solution"

def getMinimum():
	min=1000
	for i in open:
		if cost_so_far[i]<min:
			min=cost_so_far[i]
			min_node=i
	open.remove(min_node)
	return min_node
	
def displayAns():
	
		path=end
		print end, u"\u2193"
		while came_from[path] !=start:
			print came_from[path], u"\u2193"
			ans.extend([came_from[path]])
			path=came_from[path]
		print start
		print cost_so_far[end]

		board[start[0]-1][start[1]-1]="S"
		board[end[0]-1][end[1]-1]="D"

		i=len(ans)
		i-=1
		pos=1
		while i>=0:
			temp=ans[i]
			board[temp[0]-1][temp[1]-1]=pos
			pos+=1
			i-=1

		for i in range(0,8):
			line=""
			for j in range(0,8):
				line=line+str(board[i][j])+" "
			print line


	
print  "Enter Starting Position:"
a=int(raw_input())
b=int(raw_input())
if a >8 or a<1 or b >8 or b <1:
	print "Range out of bounds"
	exit()
start=(a,b)
print  "Enter Destination Position:"
a=int(raw_input())
b=int(raw_input())
if a >8 or a<1 or b >8 or b <1:
	print "Range out of bounds"
	exit()
end=(a,b)
cost_so_far[start]=0
came_from[start]=(-1,-1)
open.extend([start])
solveGame()
