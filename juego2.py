import pygame
from time import sleep
from classes import *
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
from buttons import buttons


class mando:
    def __init__(self,X,Y,height,horizontal):
        self.buttons_list = []
        self.showing = True
        self.keys ={}
        self.teams = {}
        self.actions = {}
        button1 = buttons(-120/800.0 * X + horizontal,100/ 800.0 * Y + height,3,0,X / 10,Y / 20)
        self.buttons_list.append(button1)
        self.keys["L"] = button1
        self.teams["L"]=1
        button2 = buttons(40/ 800.0 * X+ horizontal,100/ 800.0 * Y+ height,3,0,X / 10,Y / 20)
        self.buttons_list.append(button2)
        self.keys["R"] = button2
        self.teams["R"] = 2
        self.actions["R"]="shoot"
        self.actions["L"]="shoot"
        button1 = buttons(160/ 800.0 * X+ horizontal, height,2,1,X / 20,Y / 20)
        button2 = buttons(240 / 800.0 * X+ horizontal, height,2,1,X / 20,Y / 20)
        button3 = buttons(200/ 800.0 * X+ horizontal,-40 /800.0 * Y +height,2,1,X / 20,Y / 20)
        button4 = buttons(200/ 800.0 * X+ horizontal,40/ 800.0 * Y+ height,2,1,X / 20,Y / 20)
        self.buttons_list.append(button1)
        self.buttons_list.append(button2)
        self.buttons_list.append(button3)
        self.buttons_list.append(button4)
        self.keys["R_down"] = button4
        self.keys["R_up"] = button3
        self.keys["R_left"] = button1
        self.keys["R_right"] = button2
        self.teams["R_down"] = 2
        self.teams["R_up"] = 2
        self.teams["R_left"] = 2
        self.teams["R_right"] = 2

        self.actions["R_down"] = "brake"
        self.actions["R_up"] = "accelerate"
        self.actions["R_left"] = "left"
        self.actions["R_right"] = "right"

        button1 = buttons(-280/ 800.0 * X+ horizontal,height,1,1,X / 20,Y / 20)
        button2 = buttons(-200/ 800.0 * X+ horizontal,height,1,1,X / 20,Y / 20)
        button3 = buttons(-240/ 800.0 * X+ horizontal,-40 /800.0 * Y +height,1,1,X / 20,Y / 20)
        button4 = buttons(-240/ 800.0 * X+ horizontal,40/ 800.0 * Y+ height,1,1,X / 20,Y / 20)
        self.buttons_list.append(button1)
        self.buttons_list.append(button2)
        self.buttons_list.append(button3)
        self.buttons_list.append(button4)
        self.keys["L_down"] = button4
        self.keys["L_up"] = button3
        self.keys["L_left"] = button1
        self.keys["L_right"] = button2
        self.teams["L_down"] = 1
        self.teams["L_up"] = 1
        self.teams["L_left"] = 1
        self.teams["L_right"] = 1

        self.actions["L_down"] = "brake"
        self.actions["L_up"] = "accelerate"
        self.actions["L_left"] = "left"
        self.actions["L_right"] = "right"
    def reset(self):
        for i in self.buttons_list:
            i.reset()
    def show_hide(self):
        self.showing = not self.showing
    def show(self,screen,pos = None):
     
     if(self.showing ==True):
        
        
        if(pos != None):
            print(pos)
            for i in self.buttons_list:
                
                if(i.rect.collidepoint(pos)):
                    if(not i.pressed):
                        i.press()
                    else:
                        i.reset()
        for i in self.buttons_list:
            i.show(screen)
    
def select(mando):
 pos =None
 for event in pygame.event.get():
    if(event.type == pygame.KEYDOWN ):
            
            if (event.key == pygame.K_ESCAPE):
                return -1
            if (event.key == pygame.K_w):
                mando.keys["L_up"].press()
            if (event.key == pygame.K_s):
                mando.keys["L_down"].press()
            if (event.key == pygame.K_a):
                mando.keys["L_left"].press()
            if (event.key == pygame.K_d):
                mando.keys["L_right"].press()
            if (event.key == pygame.K_UP):
                mando.keys["R_up"].press()
            if (event.key == pygame.K_DOWN):
                mando.keys["R_down"].press()
            if (event.key == pygame.K_LEFT):
                mando.keys["R_left"].press()
            if (event.key == pygame.K_RIGHT):
                mando.keys["R_right"].press()
            if (event.key == pygame.K_SPACE):
                mando.keys["L"].press()
            if (event.key == pygame.K_RCTRL):
                mando.keys["R"].press()
            if (event.key == pygame.K_t):
                mando.showing =not mando.showing
            
    if( event.type == pygame.KEYUP ):
            
            if (event.key == pygame.K_w):
                mando.keys["L_up"].reset()
            if (event.key == pygame.K_s):
                mando.keys["L_down"].reset()
            if (event.key == pygame.K_a):
                mando.keys["L_left"].reset()
            if (event.key == pygame.K_d):
                mando.keys["L_right"].reset()
            if (event.key == pygame.K_UP):
                mando.keys["R_up"].reset()
            if (event.key == pygame.K_DOWN):
                mando.keys["R_down"].reset()
            if (event.key == pygame.K_LEFT):
                mando.keys["R_left"].reset()
            if (event.key == pygame.K_RIGHT):
                mando.keys["R_right"].reset()
            if (event.key == pygame.K_SPACE):
                mando.keys["L"].reset()
            if (event.key == pygame.K_RCTRL):
                mando.keys["R"].reset()
    if(event.type == pygame.MOUSEBUTTONDOWN or  event.type == pygame.MOUSEBUTTONUP):
            pos =pygame.mouse.get_pos()
 return pos

       
def main():
    X=800
    Y=800
    Xscale=40
    Yscale=40
    screen = pygame.display.set_mode((800,800))
    game = pygame.init()
    buttons_list =[]
    m = mando(800,800,600,400)
    mimapa = mapa(X,Y,Xscale,Yscale)
    mimapa.createmap()
    
    team1 = teams(randomColor(),1)
    team2= teams(randomColor(),2)
    iters = 0
    
    mimapa.create_planes(mimapa.ground +mimapa.grasslands + mimapa.desserts,1,team1)
           
    mimapa.create_planes(mimapa.ground +mimapa.grasslands + mimapa.desserts,1,team2)
 #   mimapa.create_tanks(mimapa.ground +mimapa.grasslands + mimapa.desserts,1,team1)
 #   mimapa.create_tanks(mimapa.ground +mimapa.grasslands + mimapa.desserts,1,team2)
    while(1):
        
 #       pygame.draw.rect(screen,BLACK,(0,0,800,800))
        mimapa.show(screen)
        if(iters > 50000):
            return
        iters = iters + 1
        pos = select(m)
       # if(pos == None):
 #           m.reset()
        
        if(pos == -1):
            return -1
        
        for i in mimapa.planes :
                i.act_manual(screen,m,mimapa)
        for i in mimapa.shots + mimapa.explosions:
            i.act(screen,mimapa)
        m.show(screen,pos)
 #       if(iters %20 == 0):
#            m.show_hide()
           
            
       
            
        
        pygame.display.update()
 #       sleep(0.1)
main()

    
