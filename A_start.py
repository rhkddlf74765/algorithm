from __future__ import print_function
import matplotlib.pyplot as plt
import math
 
class AStarGraph(object):
	#Define a class board like grid with two barriers
 
	def __init__(self):   ##### 장벽(장애물)위치 설정
		self.barriers = []
		self.barriers.append([(2,4),(2,5),(2,6),(3,6),(4,6),(5,6),(5,5),(5,4),(5,3),(5,2),(4,2),(3,2)])
 
	def heuristic(self, start, goal):
		#도착점과 해당점과의 휴리스틱 함수
		dx = abs(start[0] - goal[0])
		dy = abs(start[1] - goal[1])
		return math.sqrt((dx*dx)+(dy*dy))
 
	def get_vertex_neighbours(self, pos): #pos는 3x3사각형의 중간 좌표를 의미(주위의 좌표를 구하고자)
		n = []   #주위 이웃 픽셀의 좌표
		for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:### 3x3의 사각형의 좌표하나하나 구함
			x2 = pos[0] + dx
			y2 = pos[1] + dy
			if x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7:
				continue   # 그리드화면을 넘어가는 좌표는 손절
			n.append((x2, y2))    ### 넘어가지 않는 좌표는 n이라는 리스트에 저장함
		return n
 
	def move_cost(self, a, b):   #a와 b간 거리를 구함
		for barrier in self.barriers:     
			if b in barrier:        #b가 장벽위치에 있다면....
				return 100          #의도적으로 높은 cost부여
			else :
				dxx=abs(b[0]-a[0])      #b가 장벽위치에 있지 않다면 a와b의 일반적인 거리를 구함
				dyy=abs(b[1]-a[1])
				distance=math.sqrt(dxx*dxx+dyy*dyy)
				return distance   
 
def AStarSearch(start, end, graph):## 좌표, 좌표, 클래스
 
	G = {} #Actual movement cost to each position from the start position  g(x)
	F = {} #Estimated movement cost of start to end going via this position h(x)
 
	#Initialize starting values
	######    딕셔너리로 각각의 지점의 g(x)와 h(x)값을 저장함
	G[start] = 0
	F[start] = graph.heuristic(start, end)
 
	closedVertices = set()  ### 이미 지난 공간
	openVertices = set([start])   ###   열린 공간[start]는 좌표를 의미함
	cameFrom = {}
 
	while len(openVertices) > 0: # 열린 공간이 없으면 끝
		#열린 리스트에서 점수가 가장 낮은 사각형의 좌표를 가져옴
		current = None
		currentFscore = None
		for pos in openVertices:
			if current is None or F[pos] < currentFscore:   ##해당위치의 휴리스틱이 저장되있던 것보다 작으면...
				currentFscore = F[pos]
				current = pos
 
		#도착점에 도달했는가 ????
		if current == end:
			#뒤로 가면서 경로 재추적
			path = [current]
			while current in cameFrom:
				current = cameFrom[current]
				path.append(current)
			path.reverse()
			return path, F[end] #끝
 
		#현재 꼭짓점을 닫힘으로 표시
		openVertices.remove(current)  #열린 에서 제거
		closedVertices.add(current)   ## 닫힘에 추가
 
############주위의 비용 업데이트##########################3
		for neighbour in graph.get_vertex_neighbours(current):  ##현재위치를 포함하는 3x3사각형 테스트
			if neighbour in closedVertices:
				continue #닫힌 구간에 속해있는 좌표는 이미 작업을 처리했다는 증거이므로 건너뜀
			else :
				candidateG = G[current] + graph.move_cost(current, neighbour)
 
			if neighbour not in openVertices:  # 열린공간에 없음
				openVertices.add(neighbour)    #열린공간에 추가
			elif candidateG >= G[neighbour]:
				continue #새로운 데이터 candidateG는 쓸모없음이 판명됨
 
			cameFrom[neighbour] = current #딕셔너리{이웃 : 현재}로 저장
			G[neighbour] = candidateG  #이웃의 거리 저장
			H = graph.heuristic(neighbour, end)
			F[neighbour] = G[neighbour] + H  #이웃 f(x)=g(x)+h(x)
 
	raise RuntimeError("A* failed to find a solution")
 
if __name__=="__main__":
	graph = AStarGraph()
	result, cost = AStarSearch((0,0), (7,7), graph)
	print ("route", result)
	print ("cost", cost)
	plt.plot([v[0] for v in result], [v[1] for v in result])
	for barrier in graph.barriers:
		plt.plot([v[0] for v in barrier], [v[1] for v in barrier])
	plt.xlim(-1,8)
	plt.ylim(-1,8)
	plt.show()