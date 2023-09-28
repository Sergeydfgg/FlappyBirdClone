from os import path

import pygame
import bird
import walls
import button
import slider
import text_field
import grid
from display import Fon, dis, dis_width, dis_height

pygame.init()

game_close = False
start_menu = True
settings_menu = False
result_menu = False
player_bird = bird.Bird()
test_wall = [walls.Walls(200 + i*170) for i in range(50)]
clock = pygame.time.Clock()
score_font = pygame.font.SysFont("comicsansms", 35)
score_point = 0
curr_difficult = 'Normal'

difficult_list = {'Normal': 'Hard', 'Hard': 'Impossible', 'Impossible': 'BIRD GOD', 'BIRD GOD': 'Normal'}


def start_button():
    global start_menu

    start_menu = False
    game_start()


def sett_button():
    global settings_menu
    global start_menu

    start_menu = False
    settings_menu = True


def result_button():
    global result_menu
    global start_menu

    start_menu = False
    result_menu = True


def exit_button():
    global start_menu
    global game_close

    start_menu = False
    game_close = True


def back_button():
    global start_menu
    global settings_menu
    global result_menu

    start_menu = True
    settings_menu = False
    result_menu = False


def reset_button():
    global result_grid_dict

    result_grid_dict = {"Player": [], "Best score": []}
    save_results()
    result_grid.update_source(result_grid_dict)
    result_grid.prepare_source()


def set_difficult():
    global curr_difficult

    curr_difficult = difficult_list[curr_difficult]
    btn_list_settings[1] = button.Button(280, 90, 200, 50, curr_difficult, set_difficult, True)


btn_list = [
            button.Button(200, 100, 200, 50, 'Start', start_button, is_italic=False),
            button.Button(200, 170, 200, 50, 'Settings', sett_button, is_italic=False),
            button.Button(200, 250, 200, 50, 'Results', result_button, is_italic=False),
            button.Button(200, 320, 200, 50, 'Exit', exit_button, is_italic=False)
            ]

btn_list_settings = [button.Button(10, 445, 125, 45, "Back", back_button, font_size=30)]

btn_list_results = [button.Button(10, 445, 125, 45, "Back", back_button, font_size=30),
                    button.Button(dis_width / 2 - 125 / 2, 445, 125, 45, "Reset", reset_button, font_size=30)]

slider = slider.Slider(175, 295, 350, 50, 100)
text_name = text_field.TextFiled(160, 195, 200, 50, 35)

result_grid = grid.Grid(col=2, rol=6, x=(dis_width / 2 - 200), y=(dis_height / 2 - 50*3),
                        width=200, height=50, source="Data/result_grid.txt", fon_color="orange",
                        border_color=(0, 128, 0), font_size=20)
result_grid_dict = result_grid.prepare_source()


def save_settings():
    settings_path = "Data/settings.txt"
    with open(settings_path, "w") as file:
        file.write(f"name={text_name.text}\n"
                   f"volume={int(slider.slider_value)}\n"
                   f"difficult={curr_difficult}\n")


def save_results():
    global score_point

    if text_name.text not in result_grid_dict["Player"]:
        result_grid_dict["Player"].append(text_name.text)
        result_grid_dict["Best score"].append(score_point)
    for index, cur_player in enumerate(result_grid_dict["Player"]):
        if cur_player == text_name.text:
            result_grid_dict["Best score"][index] = max(score_point, int(result_grid_dict["Best score"][index]))


def update_settings():
    global curr_difficult

    settings_path = "Data/settings.txt"
    if path.exists(settings_path):
        with open(settings_path, "r") as file:
            for cur_line in file:
                if cur_line.split("=")[0] == "name":
                    text_name.text = cur_line.split("=")[1].strip()
                elif cur_line.split("=")[0] == "volume":
                    slider.slider_value = cur_line.split("=")[1].strip()
                elif cur_line.split("=")[0] == "difficult":
                    curr_difficult = cur_line.split("=")[1].strip()
                    btn_list_settings.append(button.Button(280, 90, 200, 50, curr_difficult, set_difficult))
    else:
        btn_list_settings.append(button.Button(280, 90, 200, 50, curr_difficult, set_difficult))


def game_loop():
    global start_menu
    global game_close
    global score_point

    cur_fon.draw_fon()
    pygame.draw.rect(dis, "black", player_bird.make_bird())
    for wall in test_wall:
        pygame.draw.rect(dis, "green", wall[0])
        pygame.draw.rect(dis, "green", wall[1])
        wall.wall_move()
        if wall.x_pos <= -280:
            test_wall.remove(wall)
        if len(test_wall) <= 49:
            test_wall.append(walls.Walls(100 + 49 * 170))
        if player_bird.is_collide(wall[0], wall[1]):
            save_results()
            result_grid.update_source(result_grid_dict)
            result_grid.prepare_source()
            start_menu = True
        if player_bird.pos_x == wall.x_pos:
            score_point += 1
    your_score(score_point)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_results()
            result_grid.update_source(result_grid_dict)
            result_grid.prepare_source()
            game_close = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_bird.state = "jump"

    if player_bird.pos_y <= 0 or player_bird.pos_y >= 500:
        save_results()
        result_grid.update_source(result_grid_dict)
        result_grid.prepare_source()
        start_menu = True
    if player_bird.state == "jump":
        player_bird.bird_jump()
    elif player_bird.state == "fall":
        player_bird.bird_fall()


def your_score(score):
    value = score_font.render(str(score), True, (128, 0, 0))
    dis.blit(value, [237, 10])


def settings_name():
    settings_font = pygame.font.SysFont("comicsansms", 25)
    difficult = settings_font.render("Уровень сложности -", True, "White")
    volume = settings_font.render("Громкость -", True, "White")
    player_name = settings_font.render("Никнейм -", True, "White")
    dis.blit(difficult, [20, 100])
    dis.blit(volume, [20, 300])
    dis.blit(player_name, [20, 200])


def game_start():
    global game_close
    global player_bird
    global test_wall
    global clock
    global score_point

    game_close = False
    player_bird = bird.Bird()
    test_wall = [walls.Walls(200 + i * 170) for i in range(50)]
    clock = pygame.time.Clock()
    score_point = 0


cur_fon = Fon()
update_settings()

while not game_close:

    game_loop()

    while start_menu:
        game_start()
        cur_fon.draw_fon()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                start_menu = False
        for cur_btn in btn_list:
            cur_btn.process()
        pygame.display.update()
        clock.tick(30)

    while settings_menu:
        dis.fill("brown")
        if text_name.now_edit is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                    settings_menu = False
        settings_name()
        for cur_btn in btn_list_settings:
            cur_btn.process()
        slider.process()
        text_name.text_editing()
        pygame.display.update()

    while result_menu:
        dis.fill("brown")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                result_menu = False
        for cur_btn in btn_list_results:
            cur_btn.process()
        result_grid.draw_grid()
        pygame.display.update()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
save_settings()
save_results()
result_grid.update_source(result_grid_dict)
quit()
