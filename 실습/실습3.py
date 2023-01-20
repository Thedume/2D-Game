from pico2d import *

def handle_events():
    global running
    global dir_x, dir_y
    events = get_events()
    for event in events:
        if event.type == SDL_Quit:
            running = False
        
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1
            elif event.key == SDLK_ESCAPE:
                running = False    


open_canvas(730,400)

grass = load_image('resource/background.png')
character = load_image('resource/run_animation.png')

running = True
x = 730 // 2
y = 400 // 2
frame = 0
dir_x = 0
dir_y = 0

while running:
    clear_canvas()
    grass.draw(365,200)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()