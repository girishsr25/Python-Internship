import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
paddle_speed= 5
#====================opening file to get high score=================
try:
	hi_score = open('hiscore.txt','r+')
	hi_score = hi_score.readlines()
	hi_score = int(hi_score[0])
except:
	hi_score = 0
#======================variables====================
speed = [-3,-2,-1,1,2,3]
ball_x_speed,ball_y_speed = 6,random.choice(speed)
done = False
dy = 0 
width = 20
height = 100
p1_score = 0
p2_score = 0
x1 = 0
y1 = screen.get_height() // 2 - height //2
x2 = screen.get_width() - 20
y2 = screen.get_height() // 2 - height //2
x,y = screen.get_width() // 2,screen.get_height() // 2
radius = 10
color = (255,255,255)
red = (255,0,0)
started = False
computer = False
a = 1


#====================text writer==================
def render_multi_line(text, x, y, fsize = 10):
		hecolor = (255,255,255)
		lines = text.splitlines()
		for i, l in enumerate(lines):
			screen.blit((pygame.font.SysFont('constantia',fsize)).render(l, 0, hecolor), (x, y + fsize*i))

clock = pygame.time.Clock()
#=====================game loop====================
while not done:

		for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		                done = True
		    # ====================saving high score====================
		                hi_score = open("hiscore.txt",'r+')
		                try:
		                	load = (hi_score.readlines())
		                	if int(load[0]) < max(p1_score,p2_score):
		                		hi_score = open("hiscore.txt",'w+')
		                		hi_score.write(str(max(p1_score,p2_score)))
		                except:
		                	hi_score = open("hiscore.txt",'w+')
		                	hi_score.write(str(max(p1_score,p2_score)))
		        pressed = pygame.key.get_pressed()
		        if pressed[pygame.K_SPACE]: started = True 
		        if pressed[pygame.K_RETURN]: 
		        	computer = True
		        	started = True
		if started:

		    a+=1
		    pressed = pygame.key.get_pressed()
		    if a >= 500:
		    	a = 0
		    	if ball_x_speed < 0:
		    		ball_x_speed -= 1
		    	else:
		    		ball_x_speed += 1
		    
		    if pressed[pygame.K_UP]: y2 -= paddle_speed
		    if pressed[pygame.K_DOWN]: y2 += paddle_speed
		    if not computer:
		        if pressed[pygame.K_w]: y1 -= paddle_speed
		        if pressed[pygame.K_s]: y1 += paddle_speed

		    if computer:
		    	if y < y1 + (height // 2):
		    		y1 -= paddle_speed
		    	if y > y1 + (height // 2):
		    		y1 += paddle_speed
		    	# if y < y2 + (height // 2):
		    	# 	y2 -= paddle_speed
		    	# if y > y2 + (height // 2):
		    	# 	y2 += paddle_speed
		    
		    screen.fill((0,0,0))
		    if y1 + height > screen.get_height():
		    	y1 = screen.get_height() - height
		    if y2 + height > screen.get_height():
		    	y2 = screen.get_height() - height
		    if y1 < 0:
		    	y1 = 0
		    if y2 < 0:
		    	y2 = 0
		    x += ball_x_speed
		    y += ball_y_speed
		    #========================if ball hits paddle=======================
		    if x <= (x1 + width) and y >= y1 and y <= (y1 + height):
		    	x = width
		    	ball_x_speed = - ball_x_speed
		    if x >= x2 and y >= y2 and y <= (y2 + height):
		    	ball_x_speed = - ball_x_speed
		    	x = screen.get_width() - width
		    #======================if ball hits top or bottom wall ====================
		    if y <= 0:
		    	ball_y_speed = - ball_y_speed
		    if y >= screen.get_height():
		    	ball_y_speed = - ball_y_speed
		    #=======================if ball goes out of bounds======================
		    if x > screen.get_width():
		    	x , y = screen.get_width() // 2, screen.get_height()//2
		    	ball_x_speed = - ball_x_speed
		    	p1_score += 1
		    	x1 = 0
		    	y1 = screen.get_height() // 2 - height //2
		    	x2 = screen.get_width() - 20
		    	y2 = screen.get_height() // 2 - height //2
		    	ball_y_speed = random.choice(speed)
		    	a = 0
		    	ball_x_speed = 5
		    if x < 0:
		    	x , y = screen.get_width() // 2, screen.get_height()//2
		    	ball_x_speed = - ball_x_speed
		    	p2_score += 1
		    	x1 = 0
		    	y1 = screen.get_height() // 2 - height //2
		    	x2 = screen.get_width() - 20
		    	y2 = screen.get_height() // 2 - height //2
		    	ball_y_speed = random.choice(speed)
		    	a = 0
		    	ball_x_speed = 5
		    pygame.draw.circle(screen,red,(x,y),radius)
		    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, width, height))
		    pygame.draw.rect(screen, color, pygame.Rect(x2, y2, width, height))
		    score = "player 1 :" + str(p1_score) + " ,  player 2:" + str(p2_score)
		    render_multi_line(score,210,0,20)
		    if p1_score > int(hi_score):
		    	hi_score = p1_score
		    elif p2_score > int(hi_score):
		    	hi_score = p2_score

		    hi = 'High score:'+str(hi_score)
		    render_multi_line(hi,450,0,20)
		    ball = 'ball speed:'+str(abs(ball_x_speed))
		    render_multi_line(ball,screen.get_width() // 2 - 50,screen.get_height() - 20,20)

		else:
		    pygame.draw.circle(screen,(255,0,0),(screen.get_width() // 2,screen.get_height() // 2),200)
		    text = "Welcome to PONG!!! " + '\n\n' + " press SPACE to start "+'\n'+"      controls"+'\n\n'+"w,s for player 1"+'\n'+" up,down for player 2"+'\n\n'+"press ENTER to \n play against computer"
		    render_multi_line(text,screen.get_width()//2 - 80,screen.get_height()//2 - 100,20)
		pygame.display.flip()
		clock.tick(60)
