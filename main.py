
import pygame
root=pygame.display.set_mode((1000,1000))

clock=pygame.time.Clock()
x=[]
y=[]
rad=[]
allx=[]
ally=[]
allcolor=[]
allrad=[]
paint=0
color=[(0,0,0)]
trash=pygame.image.load("trash.png")
button=pygame.image.load("but.png")
butts=[]
for i in range(1,4):
    butts.append(pygame.image.load(str(i)+"b.png"))
butts.append(pygame.image.load("4b.png"))
class Color:
    def __init__(self,color,h,root):
        self.color=color
        self.h=h*100
        self.root=root
    def place(self):
        pygame.draw.rect(self.root,(50,50,50),(self.h-5,0,60,60))
        pygame.draw.rect(self.root,self.color,(self.h,5,50,50))
black=Color((0,0,0),1,root)
red=Color((255,0,0),2,root)
green=Color((0,255,0),3,root)
blue=Color((0,0,255),4,root)
white=Color((255,255,255),5,root)
pink=Color((255,150,150),6,root)
col=black.color
radius=2
win=0
def window():
    pygame.draw.rect(root,(0,0,0),(900-300,50,300,60))
    root.blit(butts[0],(900-275,55))
    root.blit(butts[1], (900 - (275-65), 55))
    root.blit(butts[2], (900 - (275 - 65*2), 55))
    root.blit(butts[3], (900 - (275 - 65*3), 55))
while True:
    root.fill((255,255,255))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_z:
                try:
                    del allx[-1]
                    del ally[-1]
                    del allcolor[-1]
                    del allrad[-1]
                except:
                    pass
        if i.type==pygame.MOUSEBUTTONDOWN:
            try:
                if i.pos[1] >= 165:
                    x.append(i.pos[0])
                    y.append(i.pos[1])
                    color.append(col)
                    rad.append(radius)
            except:
                pass
            if i.pos[0]>=900 and i.pos[0]<=950:
                if i.pos[1]<55:
                    allx=[]
                    ally=[]
                    allcolor=[]
                    allrad=[]
            paint=1
            if i.pos[1]<=55:
                if i.pos[0]>=red.h and i.pos[0]<=red.h+50:
                    col=red.color
                if i.pos[0]>=black.h and i.pos[0]<=black.h+50:
                    col=black.color
                if i.pos[0]>=green.h and i.pos[0]<=green.h+50:
                    col=green.color
                if i.pos[0] >= blue.h and i.pos[0] <= blue.h + 50:
                    col = blue.color
                if i.pos[0] >= white.h and i.pos[0] <= white.h + 50:
                    col = white.color
                if i.pos[0] >= pink.h and i.pos[0] <= pink.h + 50:
                    col = pink.color
                if i.pos[0] >= 800 and i.pos[0] <= 800 + 50:
                    win=1
            else:
                if win:
                    if i.pos[1]<=100:
                        if i.pos[0]>=900-275 and i.pos[0]<=900-225:
                            radius=1
                        if i.pos[0]>=900 - (275 - 65) and i.pos[0]<=900 - (275 - 65*2)+50:
                            radius=2
                        if i.pos[0]>=900 - (275 - 65*2) and i.pos[0]<=900 - (275 - 65*2)+50:
                            radius=3
                        if i.pos[0]>=900 - (275 - 65*3) and i.pos[0]<=900 - (275 - 65*3)+50:
                            radius=4

                win=0
        if i.type==pygame.MOUSEBUTTONUP:
            paint=0
            allx.append(x)
            ally.append(y)
            allcolor.append(color)
            allrad.append(rad)
            x=[]
            y=[]
            color=[]
            rad=[]
    if paint:
        try:
            if i.pos[1]>=65:
                x.append(i.pos[0])
                y.append(i.pos[1])
                color.append(col)
                rad.append(radius)
        except:
            pass
        for h in range(1, len(x)):
            pygame.draw.line(root, color[h], (x[h], y[h]), (x[h - 1], y[h - 1]), rad[h])
    for l in range(0,len(allx)):
        for i in range(1,len(allx[l])):
            pygame.draw.line(root,allcolor[l][i],(allx[l][i],ally[l][i]),(allx[l][i-1],ally[l][i-1]),allrad[l][i])
    pygame.draw.rect(root,(0,0,0),(0,60,1000,2))
    black.place()
    red.place()
    green.place()
    blue.place()
    white.place()
    pink.place()
    root.blit(button,(800,5))
    root.blit(trash,(900,5))
    if win:
        window()
    pygame.display.update()
    clock.tick(60)