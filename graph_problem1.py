def positionInGraph(pos):
	return ((pos[0] >= 0) and (pos[1] >= 0)) and ((pos[0] < rows) and (pos[1] < cols))

def positionNotVisited(pos):
	return not(pos in visited)
	
def positionIsEmpty(pos):
	return (graph[pos[0]][pos[1]]==0)
	
def getAdjacent(posx, posy):
	adjQueue = [(posx-1,posy), (posx, posy+1), (posx+1, posy), (posx, posy-1)]
	for i in adjQueue:
		if (positionInGraph(i) and positionNotVisited(i) and positionIsEmpty(i)):
			yield i 

def getOnePath(pos):
	counter = 0
	pathList = []
	processQueue = []
	if (not(positionIsEmpty(pos)) or (pos in visited)):
		return (pathList, counter)
	else:
		processQueue.append(pos)
	while (processQueue and (counter < length)):
		currentPos = processQueue.pop()
		visited.add(currentPos)
		pathList.append(currentPos)
		counter = counter + 1
		adjQueue = getAdjacent(currentPos[0],currentPos[1])
		if (not(adjQueue) and counter < length):
			pathList.pop(currentPos)
			counter -= 1
		for i in adjQueue:
			processQueue.append(i)
		
	
	print pathList
	return (pathList, counter)

def findFinalPath():
	#5 4 8
# oxoo
# xoxo
# ooxo
# xooo
# oxox

	
	for i in xrange(0,rows):
		for j in xrange(0,cols):
			path = getOnePath((i,j))
			if path[1] == length:
				return path[0]
	
	return "impossible"

visited = set()
graph = [[0,1,0,0],[1,0,1,0],[0,0,1,0],[1,0,0,0],[0,1,0,1]]

rows = 5
cols = 4
length = 8
		

findFinalPath()	
			


			

