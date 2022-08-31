import pgzrun
WIDTH = 1500
HEIGHT = 1500
TITLE = 'game'
img = '13'
left = ['9', '10', '11', '12']
right = ['13', '14', '15', '16']
up = ['5', '6', '7', '8']
down = ['1', '2', '3', '4']
gifts_pos = [(500, 650), (100, 100), (900, 550)]
score = ['table_0', 'table_1', 'table_2', 'table_3']
x, y = -400, -400
a = 0
def draw():
    screen.fill((255,192,203))
    screen.blit('im1', (x, y))
    screen.blit(img, (520, 750))
    for pos in gifts_pos:
        x_pos, y_pos = pos
        screen.blit('gift', (x_pos + x, y_pos + y))
        
    screen.blit(score[len(gifts_pos)], (970, 100))
def borders():
    global x, y
    if x < 520 and x > -928 and y < 800 and y > -676:
        return True
    else:
        return False
def wall_1():
    global x, y
    if x > -520 and x < -208 and y < 88 and y > 20:
        return True
    else:
        return False
def wall_2():
    global x, y
    if x > -520 and x < -428 and y < 560 and y > 20:
        return True
    else:
        return False
def wall_3():
    global x, y
    if x > -520 and x < 328 and y < 560 and y > 480:
        return True
    else:
        return False
def wall_4():
    global x, y
    if x > 232 and x < 328 and y < 560 and y > 20:
        return True
    else:
        return False
def wall_5():
    global x, y
    if x > -80 and x < 328 and y < 88 and y > 20:
        return True
    else:
        return False
def wall_6():
    global x, y
    if x > -80 and x < 20 and y < 284 and y > 20:
        return True
    else:
        return False
def wall_7():
    global x, y
    if x > -80 and x < 164 and y < 284 and y > 212:
        return True
    else:
        return False
    
        
def correst_pos():
    if borders() and not wall_1() and not wall_2() and not wall_3() and not wall_4() and not wall_5() and not wall_6() and not wall_7():
        return True
    else:
        return False

def Compare(pos):
    global x, y
    x_pos, y_pos = pos
    if abs(x_pos + x - 520) < 70 and abs(y_pos + y - 750) < 70:
        return True
    else:
        return False
    
def Gift():
    global x, y, gifts_pos
            
    gifts_pos = [pos for pos in gifts_pos if not Compare(pos)]
    
    
def update():
    global x, y, a, img
    if keyboard.left:
        x += 4
        if correst_pos():
            img = left[a // 3 % 4]
            a += 2
        else:
            x -= 4
    if keyboard.right:
        x -= 4
        if correst_pos():
            img = right[a // 3 % 4]
            a += 2
        else:
            x += 4
    if keyboard.up:
        y += 4
        if correst_pos():
            img = up[a // 3 % 4]
            a += 2
        else:
            y -= 4
    if keyboard.down:
        y -= 4
        if correst_pos():
            img = down[a // 3 % 4]
            a += 2
        else:
            y += 4
    
    Gift()
    
# if x < 1650:
# x += 10
# if x > -450:
# x -= 30
# if y < 1660:
# y += 10
# if y > -150:
# y -= 30
def on_mouse_down(pos, button):
    pass
pgzrun.go()