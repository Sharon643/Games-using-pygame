import pygame, sys
#classes
class Ball:
    def __init__(self,screen,color,posX,posY,radius):
        self.screen=screen
        self.color=color
        self.posX=posX
        self.posY=posY
        self.radius=radius
        self.dx=0
        self.dy=0
        self.show()

    def show(self):
        pygame.draw.circle(self.screen,self.color,(self.posX,self.posY),self.radius)

    def start_moving(self):
        self.dx=5
        self.dy=2

    def move(self):
        self.posX+=self.dx
        self.posY+=self.dy
    def paddle_collision(self):
        self.dx=-self.dx
    def wall_collision(self):
        self.dy=-self.dy
    def restart_pos(self):
        self.posX=width//2
        self.posY=hght//2
        ball.show()
    
class Paddle:
    def __init__(self,screen,color,posX,posY,width,height):
        self.screen=screen
        self.color=color
        self.posX=posX
        self.posY=posY
        self.width=width
        self.height=height
        self.state='stopped'
        self.show()
    
    def show(self):
        pygame.draw.rect(self.screen,self.color,(self.posX,self.posY,self.width,self.height))
    def move(self):
        if self.state=='up':
            self.posY-=10
        elif self.state=='down':
            self.posY+=10
    def clamp(self):
        if self.posY<=0:
            self.posY=0
        elif self.posY+self.height>=hght:
            self.posY=hght-self.height
    def restart_paddle_pos(self):
        self.posY=hght//2 - self.height//2
        self.show()
class Score:
    def __init__(self,screen,points,posX,posY):
        self.screen=screen
        self.points=points
        self.posX=posX
        self.posY=posY
        self.font=pygame.font.SysFont("monospace",60,bold=True)
        self.label=self.font.render(self.points,0,white)
        self.show()
    def show(self):
        self.screen.blit(self.label,(self.posX - self.label.get_rect().width//2,self.posY))
    def increase(self):
        points=int(self.points)+1
        self.points=str(points)
        self.label=self.font.render(self.points,0,white)
    def restart(self):
        self.points='0'
        self.label=self.font.render(self.points,0,white)

                    
class Collission:
    def between_ball_and_paddle1(self,ball,paddle1):
        if ball.posY + ball.radius > paddle1.posY and ball.posY - ball.radius < paddle1.posY + paddle1.height:
            if ball.posX - ball.radius <= paddle1.posX +paddle1.width:
                return True
        return False
    def between_ball_and_paddle2(self,ball,paddle2):
         if ball.posY + ball.radius > paddle2.posY and ball.posY - ball.radius < paddle2.posY + paddle2.height:
            if ball.posX + ball.radius >= paddle2.posX:
                return True
         return False
    def between_ball_and_wall(self,ball) :
        if ball.posY + ball.radius <= 0:
            return True
        if ball.posY+ball.radius >= hght:
            return True
        return False
    def check_point_player1(self,ball,):
        return ball.posX - ball.radius >= width
    def check_points_player2(self,ball):
        return ball.posX+ball.radius <= 0
pygame.init()
width=900
hght=500
white=(255,255,255)
black=(0,0,0)
screen=pygame.display.set_mode((width,hght)) 
clock = pygame.time.Clock()

pygame.display.set_caption("PING PONG")
def paint_back():
    screen.fill(black)
    pygame.draw.line(screen,white,(width//2,0),(width//2,hght),5)
paint_back()

#objects
ball=Ball(screen,white,width//2,hght//2,10)

#ball.show()
paddle1=Paddle(screen,white,15,hght//2-60,20,120)
paddle2=Paddle(screen,white,width-20-15,hght//2-60,20,120)
collission=Collission()

score1=Score(screen,'0',width//4,15)
score2=Score(screen,'0',width-width//4,15)
#variables
playing=False

#mainloop
while True:                                                                       
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            sys.exit()
        if events.type==pygame.KEYDOWN:
            if events.key==pygame.K_SPACE:
                ball.start_moving()
                playing=True
            if events.key==pygame.K_r:
                score1.restart()
                score2.restart()
                paint_back()
                paddle1.restart_paddle_pos()
                paddle2.restart_paddle_pos()

            if events.key==pygame.K_w:
                paddle1.state='up'
            if events.key==pygame.K_s:
                paddle1.state='down'
            if events.key==pygame.K_i:
                paddle2.state='up'
            if events.key==pygame.K_k:
                paddle2.state='down'
        if events.type==pygame.KEYUP:
            paddle1.state='stopped'
            paddle2.state='stopped'

    if playing:
        paint_back()
        ball.move()
        ball.show()
        paddle1.move()
        paddle1.clamp()
        paddle1.show()

        paddle2.move()
        paddle2.clamp()
        paddle2.show()

        

        if collission.between_ball_and_paddle1(ball,paddle1):
            ball.paddle_collision()
        if collission.between_ball_and_paddle2(ball,paddle2):
            ball.paddle_collision()
        if collission.between_ball_and_wall(ball):
            ball.wall_collision()
        if collission.check_point_player1(ball):
            score1.increase()
            ball.restart_pos()
            playing=False
            #ball.show()
        if collission.check_points_player2(ball):
            score2.increase()
            ball.restart_pos()
            playing=False
            #ball.show()
    if playing==False and score1.points =='0' and score2.points =='0':
        font = pygame.font.SysFont("monospace", 25, bold=True)
        msg = font.render("Press SPACE to start", True, white)
        screen.blit(msg, (width//2 - msg.get_width()//2, msg.get_height()//2))
    if playing==False and score1.points =='5' or score2.points =='5':
        font = pygame.font.SysFont("monospace", 25, bold=True)
        msg = font.render("Press R to restart", True, white)
        screen.blit(msg, (width//2 - msg.get_width()//2, msg.get_height()//2))
    score1.show()
    score2.show()
    pygame.display.update()
    clock.tick(60)
