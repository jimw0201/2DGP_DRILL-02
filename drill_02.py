from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=0
radian=250

for count in range(0, 100) : 
        clear_canvas_now()
        grass.draw_now(400, 30) 
        character.draw_now(x, 90)
        x += 4
        delay(0.005) 
while(1) :
    #triangle move
    for count in range(0, 100) : 
        clear_canvas_now()
        grass.draw_now(400, 30) 
        character.draw_now(x, 90)
        x += 4
        delay(0.005) 
    for count in range(0, 200) : 
        clear_canvas_now()
        grass.draw_now(400, 30) 
        character.draw_now(x, 90 + y)
        x -= 2
        y += 2
        delay(0.005) 
    for count in range(0, 200) : 
        clear_canvas_now()
        grass.draw_now(400, 30) 
        character.draw_now(x, 90 + y)
        x -= 2
        y -= 2
        delay(0.005) 
    for count in range(0, 100) : 
        clear_canvas_now()
        grass.draw_now(400, 30) 
        character.draw_now(x, 90 + y)
        x += 4
        delay(0.005)
    
    #circle move
    for theta in range(-90, 270) :
        clear_canvas_now()
        grass.draw_now(400, 30) 
        character.draw_now(x, 90 + y)
        x = 400 + radian * math.cos(math.radians(theta))
        y = 255 + radian * math.sin(math.radians(theta))
        delay(0.005)   
close_canvas()
