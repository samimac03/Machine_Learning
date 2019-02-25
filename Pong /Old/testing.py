import pygame
screen=pygame.display.set_mode([650, 450])
screen.fill([0, 0, 0])
red=255
blue=255
green=255
ballX=70
ballY=50
width=6
height=50
filled=0
ballOY = 3
ballOX = 3
running=True
while running:
    if ballX > 650 or ballX < 0:
        ballOX = ballOX * -1
        print "w"
    if ballY > 450 or ballY < 0:
        ballOY = ballOY * -1
        print "e"
    pygame.draw.circle(screen, [0,0,0], [ballX,ballY], 5)
    ballY=ballY+ballOY
    ballX=ballX+ballOX
    pygame.draw.circle(screen, [100,100,100], [ballX,ballY], 5)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
pygame.quit()
