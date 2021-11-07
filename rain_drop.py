import pygame as pg
import random
import time
pg.init()

background=(0,0,0)
rain_color=(255,255,200)
RAIN_NUM=65
rain_size=25
rain_vy=50
rain_vy1=10
rain_vy2=30
rain_vx=0

size  = [1000,700]
screen= pg.display.set_mode(size)
pg.display.set_caption("RAIN_DROP")
done=False
clock=pg.time.Clock()


def rain_posi():
    list_x=[None]*RAIN_NUM
    list_y=[None]*RAIN_NUM
    for i in range(RAIN_NUM):  ###무작위 좌표를 가지는 10개의 빗방울 좌표 생성
        list_x[i]=random.randint(0,1010)
        list_y[i]=random.randint(-200,300)
    result_list=[[x,y] for x,y in zip(list_x,list_y)]  ### (x,y)튜플 형태의 좌표 생성
    return result_list
class rain:
    def __init__(self,axis__list):
        self.axis__list=axis__list
    def making(self,screen,rain_vx,rain_vy,rain_color):
        for i in range(RAIN_NUM):
            pg.draw.line(screen,rain_color,[self.axis__list[i][0]+rain_vx,self.axis__list[i][1]+rain_vy+rain_size],#rain_size],\
                [self.axis__list[i][0]+rain_vx,self.axis__list[i][1]+rain_vy],2) ##pygame의 전체적인 화면, 색, 시작 위치, 끝 위치, 선 두께
    def find_limit(self):
        self.min=10000
        for i in range(RAIN_NUM):
            if self.axis__list[i][1]<self.min:
                self.min=self.axis__list[i][1]
        return self.min
    def list_up(self,rain_vy): ##리스트 요소들의 값을 속도만큼 올린 후 반환
        for i in range(RAIN_NUM):
            self.axis__list[i][1]+=rain_vy
        return self.axis__list
    
axis_list=rain_posi()
axis_list1=rain_posi()
axis_list2=rain_posi()


while not done:
    clock.tick(15) ##초당 10번의 화면 출력 이 값이 높으면 cpu 많이 잡아먹음
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done=True
    screen.fill(background)
    ########## default #####################
    # a=rain(axis_list)
    # axis_list=a.list_up(rain_vy)
    # a.making(screen,rain_vx,rain_vy,rain_color)
    # lower_value=a.find_limit()
    # if lower_value>700:
    #     axis_list=rain_posi()
    ######################################
    a=rain(axis_list)
    axis_list=a.list_up(rain_vy)
    a.making(screen,rain_vx,rain_vy,rain_color)
    lower_value=a.find_limit()
    if lower_value>300:
        axis_list=rain_posi()

    b=rain(axis_list1)
    axis_list1=b.list_up(rain_vy1)
    b.making(screen,rain_vx,rain_vy1,rain_color)
    lower_value1=b.find_limit()
    if lower_value1>300:
        axis_list1=rain_posi()

    c=rain(axis_list2)
    axis_list2=b.list_up(rain_vy2)
    c.making(screen,rain_vx,rain_vy1,rain_color)
    lower_value2=c.find_limit()
    if lower_value2>300:
        axis_list2=rain_posi()

    pg.display.flip()