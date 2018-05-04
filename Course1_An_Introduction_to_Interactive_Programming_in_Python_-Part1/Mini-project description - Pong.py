# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [0.0, 0.0]
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5
paddle1_pos = [(HEIGHT-PAD_HEIGHT)/2, (HEIGHT+PAD_HEIGHT)/2]
paddle2_pos = [(HEIGHT-PAD_HEIGHT)/2, (HEIGHT+PAD_HEIGHT)/2]
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel_x = random.randrange(120, 240)/60.0
    ball_vel_y = random.randrange(60, 180)/60.0
    if direction == RIGHT :
        ball_vel[0] = ball_vel_x * (-1)
        ball_vel[1] = ball_vel_y * (-1)
    else:
        ball_vel[0] = ball_vel_x 
        ball_vel[1] = ball_vel_y * (-1)
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos[0] = (HEIGHT-PAD_HEIGHT)/2
    paddle1_pos[1] = (HEIGHT+PAD_HEIGHT)/2
    paddle2_pos[0] = (HEIGHT-PAD_HEIGHT)/2
    paddle2_pos[1] = (HEIGHT+PAD_HEIGHT)/2  
    x = random.randrange(1,3)
    if x == 1:
        direction = LEFT
    else:
        direction = RIGHT
    spawn_ball(direction)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[0] + paddle1_vel >= 0 and paddle1_pos[1] + paddle1_vel <= 400:
        paddle1_pos[0] = paddle1_pos[0] + paddle1_vel
        paddle1_pos[1] = paddle1_pos[1] + paddle1_vel
    if paddle2_pos[0] + paddle2_vel >= 0 and paddle2_pos[1] + paddle2_vel <= 400:
        paddle2_pos[0] = paddle2_pos[0] + paddle2_vel
        paddle2_pos[1] = paddle2_pos[1] + paddle2_vel
        
    # draw paddles
    #canvas.draw_polygon([[0, (HEIGHT-PAD_HEIGHT)/2], [PAD_WIDTH, (HEIGHT-PAD_HEIGHT)/2], [0, (HEIGHT+PAD_HEIGHT)/2], [PAD_WIDTH, (HEIGHT+PAD_HEIGHT)/2]], 1, 'White', 'White')
    canvas.draw_line([PAD_WIDTH/2, paddle1_pos[0]], [PAD_WIDTH/2, paddle1_pos[1]], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH-PAD_WIDTH/2, paddle2_pos[0]], [WIDTH-PAD_WIDTH/2, paddle2_pos[1]], PAD_WIDTH, 'White')
    # determine whether paddle and ball collide    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos[0] and ball_pos[1] <= paddle1_pos[1]:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = 1.1 * ball_vel[0]
            ball_vel[1] = 1.1* ball_vel[1]
        else:
            spawn_ball(LEFT)
            score2 += 1
    elif ball_pos[1]<= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos[0] and ball_pos[1] <= paddle2_pos[1]:
            ball_vel[0] = - ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
            ball_vel[0] = 1.1 * ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score1 += 1
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # draw scores
    canvas.draw_text(str(score1), [200,100], 40, 'White')
    canvas.draw_text(str(score2), [400,100], 40, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset Game', new_game, 100)


# start frame
new_game()
frame.start()