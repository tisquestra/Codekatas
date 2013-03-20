def positionInGraph(pos):
	return ((pos[0] >= 0) and (pos[1] >= 0)) and ((pos[0] < rows) and (pos[1] < cols))

def positionNotVisited(pos, visited):
	return not(pos in visited)
	
def positionIsEmpty(pos, graph):
	return (graph[pos[0]][pos[1]]==0)
	
def getAdjacent(posx, posy, graph, visited):
	adjQueue = [(posx-1,posy), (posx, posy+1), (posx+1, posy), (posx, posy-1)]
	for i in adjQueue:
		print "Adjacent pos (%d,%d)" %(i[0],i[1])
		if (positionInGraph(i) and positionNotVisited(i, visited) and positionIsEmpty(i, graph)):
			print "Yielding (%d,%d)" %(i[0],i[1])
			yield i 

def getOnePath(pos, inputPathLength, graph, visited):
	print "Evaluating getOnePath"
	print "position: %d,%d" % (pos[0],pos[1])
	print visited
	counter = 0
	pathList = []
	processQueue = []
	if (not(positionIsEmpty(pos,graph)) or (pos in visited)):
		print "Position is not empty or visited"
		return (pathList, counter)
	else:
		processQueue.append(pos)
	while (processQueue and (counter < inputPathLength)):
		print "Processing the current entry in the queue"
		currentPos = processQueue.pop()
		print "Processing the entry %d,%d" %(currentPos[0],currentPos[1])
		visited.add(currentPos)
		pathList.append(currentPos)
		counter = counter + 1
		adjQueue = getAdjacent(currentPos[0],currentPos[1], graph, visited)
		if (not(adjQueue) and counter < inputPathLength):
			pathList.pop(currentPos)
			print "Decrementing counter %d" %(counter)
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
			path = getOnePath((i,j), length, graph, visited)
			if path[1] == length:
				return path[0]
	
	print "impossible"
	return "impossible"

visited = set()
graph = [[0,1,0,0],[1,0,1,0],[0,0,1,0],[1,0,0,0],[0,1,0,1]]

rows = 5
cols = 4
length = 8
		

findFinalPath()	
			


			

