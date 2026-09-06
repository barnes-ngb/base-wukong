angle = 135
STEP = 30
LO = 15
HI = 165

def move_to(a):
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, a)
    basic.show_number(a)

def on_button_a():
    global angle
    angle = min(HI, angle + STEP)
    move_to(angle)

input.on_button_pressed(Button.A, on_button_a)

def on_button_b():
    global angle
    angle = max(LO, angle - STEP)
    move_to(angle)

input.on_button_pressed(Button.B, on_button_b)

move_to(angle)
