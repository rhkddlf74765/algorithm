#include<stdio.h>

int array[6][6] = { {0,2,5,1,1000,1000},{2,0,3,2,1000,1000},{5,3,0,3,1,5},{1,2,3,0,1,1000},
		{1000,1000,1,1,0,2},{1000,1000,5,1000,2,0} };
int minlo; //최솟값 인덱스
int visit_check[6] = { 0,0,0,0,0,0 };// 이미 지나간 노드는 1로 표시 아직 지나가지 않았으면 0
int dis[6];

int finding_min(int size)// 방문하지 않았던 노드와의 최소거리
{
	int min;
	min = 1000;  
	for (int i = 1; i < size; i++)
	{
		if ((min > dis[i]) && visit_check[i]==0)
		{
			min = dis[i];
			minlo = i;
		}
	}
	return minlo;
}

void dijkstra(int start)// 몇번째 부터 시작하는지 array칸 참고를 위한 변수
{
	for (int i = 0; i < 6; i++)
	{
		dis[i] = array[start][i];//dis는 start에서 시작할때 각 노드까지의 거리
	}
	visit_check[start] = 1; //visit_check에서 1로 한번 체크했다고 남김
	for (int i = 0; i < 4; i++)
	{
		int al_check = finding_min(6);
		visit_check[al_check] = 1;///////*******************************************8
		for (int j = 0; j < 6; j++)
		{
			if (visit_check[j] == 0)
			{////////////////////////////////////*************************88
				if (dis[al_check] + array[al_check][j] < dis[j])//dis[al_check]는 처음에서 가장가까운 노드까지의 거리
				//// ex) 1-->4 + 4-->5 < 1-->5 이면 전자가 최소거리이므로 저장
				{
					dis[j] = dis[al_check] + array[al_check][j];//최소거리는 새롭게 저장

				}
			}
		}
	}
}
int main(void)
{
	dijkstra(0);
	for (int i = 0; i < 6; i++) 
	{
		printf("%d   ", dis[i]);
	}
	printf("\n");
	printf("최단경로는 %d", dis[5]);
	
	return 0;
}