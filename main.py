angle = 45
STEP = 15
LO = 15
HI = 90

CAGE_L_OPEN = 30
CAGE_L_SHUT = 120
CAGE_R_OPEN = 150
CAGE_R_SHUT = 60
cage_shut = False

def move_to(a):
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, a)
    basic.show_number(a)

def set_cage(shut):
    if shut:
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, CAGE_L_SHUT)
        basic.pause(300)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S2, CAGE_R_SHUT)
        basic.show_icon(IconNames.Square)
    else:
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, CAGE_L_OPEN)
        basic.pause(300)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S2, CAGE_R_OPEN)
        basic.show_icon(IconNames.SmallSquare)

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

def on_logo_pressed():
    global cage_shut
    cage_shut = not cage_shut
    set_cage(cage_shut)

input.on_logo_event(TouchButtonEvent.Pressed, on_logo_pressed)

def on_shake():
    global cage_shut
    cage_shut = False
    set_cage(cage_shut)

input.on_gesture(Gesture.Shake, on_shake)

set_cage(False)
basic.pause(300)
move_to(angle)
