#include<stdio.h>

int array[6][6] = { {0,2,5,1,1000,1000},{2,0,3,2,1000,1000},{5,3,0,3,1,5},{1,2,3,0,1,1000},
		{1000,1000,1,1,0,2},{1000,1000,5,1000,2,0} };
int minlo; //�ּڰ� �ε���
int visit_check[6] = { 0,0,0,0,0,0 };// �̹� ������ ���� 1�� ǥ�� ���� �������� �ʾ����� 0
int dis[6];

int finding_min(int size)// �湮���� �ʾҴ� ������ �ּҰŸ�
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

void dijkstra(int start)// ���° ���� �����ϴ��� arrayĭ ���� ���� ����
{
	for (int i = 0; i < 6; i++)
	{
		dis[i] = array[start][i];//dis�� start���� �����Ҷ� �� �������� �Ÿ�
	}
	visit_check[start] = 1; //visit_check���� 1�� �ѹ� üũ�ߴٰ� ����
	for (int i = 0; i < 4; i++)
	{
		int al_check = finding_min(6);
		visit_check[al_check] = 1;///////*******************************************8
		for (int j = 0; j < 6; j++)
		{
			if (visit_check[j] == 0)
			{////////////////////////////////////*************************88
				if (dis[al_check] + array[al_check][j] < dis[j])//dis[al_check]�� ó������ ���尡��� �������� �Ÿ�
				//// ex) 1-->4 + 4-->5 < 1-->5 �̸� ���ڰ� �ּҰŸ��̹Ƿ� ����
				{
					dis[j] = dis[al_check] + array[al_check][j];//�ּҰŸ��� ���Ӱ� ����

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
	printf("�ִܰ�δ� %d", dis[5]);
	
	return 0;
}