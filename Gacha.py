import random
import copy
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "QAQ"
import pygame

print("氦，MetaMiku哒唷~各位同志们好呀~有能力的来Github支持一下呗👉https://github.com/MetaMikuAI/Gacha\n")

pygame.init();
size = width,height = 960,216 ;
screen = pygame.display.set_mode(size); 
clock = pygame.time.Clock();
FONT = pygame.font.Font('C:\WINDOWS\FONTS\SIMSUN.TTC', 96)
maxFPS=120
screen.fill((255,255,255))
pygame.display.flip()

MaxNum = 40 
Plan = [5,5,6,6,6,6,6]
msg = ['一','二','三','四','五','六','七']

class DataStruct:
    def __init__(self):
        self.name = ""
        self.weight = 1
    def ban(self):
        self.weight = 0

def GetWeightSum(List):
    WeightSum = 0
    for i in range(MaxNum):
        WeightSum += List[i].weight
    return WeightSum

def GetGacha(WeightSum,List):
    LuckyNumber = random.randint(1,WeightSum)
    for someone in List:
        LuckyNumber -= someone.weight
        if LuckyNumber <= 0:
            break
    return someone

def GachaDisplay(pygame,screen,List,WeightSum,Num):
    List_ = copy.deepcopy(List)
    Group = []
    for i in range(Num):
        someone = GetGacha(WeightSum,List_)
        someone.ban()
        Group.append(someone)
    ScreenFlash(pygame,screen,Group,-1)

def ScreenFlash(pygame,screen,Group,order):
    screen.fill((255,255,255))
    string = ''
    for someone in Group:
        string += someone.name
        string += ' '
    if order == -1:
        print('\r正在随机中：'+string,end = '')
    else:
        print('\r第'+msg[order]+'轮中奖：'+string)
        
    text_surface=FONT.render(string, 1, (0,0,0))
    screen.blit(text_surface,(64, 32))
    pygame.display.flip()
    pygame.display.set_caption('Gacha');

if __name__ == '__main__':
    mouse=0
    List = [DataStruct() for i in range(MaxNum)]
    for i in range(MaxNum):
        List[i].name = str(i+1) if i+1 > 9 else (' '+str(i+1))
    
    WeightSum = GetWeightSum(List)
    Mouse = 0
    order = 0
    while True:
        clock.tick(maxFPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Mouse = 1
            elif event.type == pygame.MOUSEBUTTONUP:
                Mouse = 0
                Group = []
                for i in range(Plan[order]):
                    someone = GetGacha(WeightSum,List)
                    someone.ban()
                    WeightSum = GetWeightSum(List)
                    Group.append(someone)
                ScreenFlash(pygame,screen,Group,order)
                order += 1
        if order == 7:
            break
        if Mouse == 1:
            GachaDisplay(pygame,screen,List,WeightSum,Plan[order])
    while True:
        clock.tick(maxFPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                pygame.quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.MOUSEBUTTONUP):
                print('抽奖已结束')
                screen.fill((255,255,255))
                pygame.display.flip()