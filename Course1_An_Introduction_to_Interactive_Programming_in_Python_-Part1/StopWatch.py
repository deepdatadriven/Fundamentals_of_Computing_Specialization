# template for "Stopwatch: The Game"
import simplegui
# define global variables
interval = 100
time_run = 0
time_show = '0:00.0'
total_click = 0
win_click = 0
sec_tens = 0
result = 'Wins: 0/Tried: 0'
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time_run):
    global sec_tens
    sec_tens = time_run % 10
    sec = ((time_run - sec_tens)/10) % 60
    min = ((time_run - sec_tens)/10) / 60
    if len(str(sec)) == 1:
        time_show = str(min) + ':0' + str(sec) + '.' + str(sec_tens)
        return time_show
    else:
        time_show = str(min) + ':' + str(sec) + '.' + str(sec_tens)
        return time_show
    #pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer.start()

def stop_timer():
    global total_click
    global win_click
    global sec_tens
    if timer.is_running():
        total_click = total_click + 1
        if sec_tens == 0:
            win_click = win_click + 1
        timer.stop()
        
            
def reset_timer():
    global time_run
    global time_show
    global total_click
    global win_click
    time_show = '0:00.0'
    total_click = 0
    win_click = 0
    time_run = 0
    min = 0
    sec = 0
    sec_tens = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():    
    global time_run
    global time_show
    time_run = time_run + 1
    time_show = format(time_run)    

# define draw handler
def draw(canvas):
    canvas.draw_text(time_show, [200,160], 42, "#FFB90F")
    global result
    result = 'Wins: ' + str(win_click) + '/Tried: ' + str(total_click)
    canvas.draw_text(result, [300,20], 20, "Green") 
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 500,300)
frame.set_canvas_background('#FFEFD5')
timer = simplegui.create_timer(interval, tick)

# register evet handlers
frame.set_draw_handler(draw)
frame.add_button('Start', start_timer, 100)
frame.add_button('Stop', stop_timer, 100)
frame.add_button('Reset', reset_timer, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
