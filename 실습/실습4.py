from pico2d import *

w, h = 730, 400

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_Quit:
            running = False
        
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, h - 3 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(w, h)

grass = load_image('resource/background.png')
character = load_image('resource/run_animation.png')
mouse_cursor = load_image('resource/mouse_cursor.png')

running = True
x = w // 2
y = h // 2
frame = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    grass.draw(365,200)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    
    frame = (frame + 1) % 10

    handle_events()
    delay(0.05)

close_canvas()