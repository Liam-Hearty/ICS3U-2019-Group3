#!/usr/bin/env python3

# Created by: Liam Hearty & Joseph Palermo
# Created on: January 2020
# This program runs "Ice Ice Baby"

import ugame
import stage
import time
import random
import constants


def splash_scene():
    image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 15)

    sprites = []
    text = []
    text3 = []
    text3_list = []
    text3 = stage.Text(width=29, height=12, font=None,
                       palette=constants.ICE_ICE_BABY_PALETTE, buffer=None)
    text3.move(30, 6)
    text3.text("Ice Ice Baby")
    text.append(text3)
    text4 = []
    text4_list = []
    text4 = stage.Text(width=17, height=5, font=None,
                       palette=constants.ICE_ICE_BABY_PALETTE, buffer=None)
    text4.move(16, 116)
    text4.text("Press A To Begin")
    text.append(text4)
    # text5 = []
    # text5_list = []
    # text5 = stage.Text(width=17, height=5, font=None,
    #                    palette=constants.ICE_ICE_BABY_PALETTE, buffer=None)
    # text5.move(16, 10)
    # text5.text("Created By: Liam Hearty & Joseph Palermo")
    # text.append(text5)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:
            menu_scene()
        game.tick()


def menu_scene():
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_2, constants.SCREEN_X,
                            constants.SCREEN_Y)
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # get sound ready
    boot_up = open("boot_up.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    sprites = []
    text = []
    text2_list = []
    text1 = stage.Text(width=29, height=12, font=None,
                       palette=constants.NEW_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)
    text2 = stage.Text(width=15, height=5, font=None,
                        palette=constants.NEW_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("Press Start")
    text.append(text2)

    sound.play(boot_up)

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + sprites + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START != 0:
            game_scene()
        game.tick()


def game_scene():
    vilheleme_list = []  # 2nd or 3rd sprite
    water_sprites = []  # 4th or 5th sprite
    ice_sprites = []  # 6th sprite
    key_list = []  # 7th sprite
    door_list = []  # 8th sprite
    finish_list = []  # 10th sprite
    wall_sprites = []  # 11th sprite

    # get sound ready
    press_start_audio = open("press_start_audio.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # score
    score = 0
    level = 1

    # buttons that keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    up_button = constants.button_state["button_up"]
    down_button = constants.button_state["button_up"]
    left_button = constants.button_state["button_up"]
    right_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    image_bank_1 = stage.Bank.from_bmp16("iib_sprites.bmp")

    # create vilheleme
    vilheleme = stage.Sprite(image_bank_1, 2, 10, 60)
    vilheleme_list.append(vilheleme)  # insert at the top of sprite list

    # create ice
    for ice_number in range(constants.TOTAL_NUMBER_OF_ICE):
        a_single_ice = stage.Sprite(image_bank_1, 6,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        ice_sprites.append(a_single_ice)

    # create walls
    for wall_number in range(constants.TOTAL_NUMBER_OF_WALLS):
        a_single_wall = stage.Sprite(image_bank_1, 11,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        wall_sprites.append(a_single_wall)

    # create water
    for water_number in range(constants.TOTAL_NUMBER_OF_WATER):
        a_single_water = stage.Sprite(image_bank_1, 4,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        water_sprites.append(a_single_water)

    # create key
    key = stage.Sprite(image_bank_1, 7, constants.OFF_SCREEN_X,
                                constants.OFF_SCREEN_Y)
    key_list.append(key)  # insert at the top of sprite list

    # create door
    door = stage.Sprite(image_bank_1, 8, constants.OFF_SCREEN_X,
                                constants.OFF_SCREEN_Y)
    door_list.append(door)  # insert at the top of sprite list

    # create finish
    finish = stage.Sprite(image_bank_1, 10, constants.OFF_SCREEN_X,
                                constants.OFF_SCREEN_Y)
    finish_list.append(finish)  # insert at the top of sprite list

    # create background
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 3)

    
    # add text at top of screen for score
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("{0}".format(score))

    # add text at top of screen for level
    level_text = stage.Text(width=20, height=15, font=None, palette=constants.LEVEL_PALETTE, buffer=None)
    level_text.clear()
    level_text.cursor(12, 0)
    level_text.move(1, 1)
    level_text.text("Level 1".format(level))

    # V If game lags, change this V
    game = stage.Stage(ugame.display, constants.FPS)

    # V add layers here V
    game.layers = vilheleme_list + water_sprites + ice_sprites + wall_sprites + key_list + door_list + finish_list + [score_text] + [level_text] + [background]
    game.render_block()

    sound.play(press_start_audio)

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_UP != 0:  # up button possible positions
            if up_button == constants.button_state["button_up"]:
                up_button = constants.button_state["button_just_pressed"]
            elif up_button == constants.button_state["button_just_pressed"]:
                up_button = constants.button_state["button_still_pressed"]
        else:
            if up_button == constants.button_state["button_still_pressed"]:
                up_button = constants.button_state["button_released"]
            else:
                up_button = constants.button_state["button_up"]

        if keys & ugame.K_DOWN != 0:  # down button possible positions
            if down_button == constants.button_state["button_up"]:
                down_button = constants.button_state["button_just_pressed"]
            elif down_button == constants.button_state["button_just_pressed"]:
                down_button = constants.button_state["button_still_pressed"]
        else:
            if down_button == constants.button_state["button_still_pressed"]:
                down_button = constants.button_state["button_released"]
            else:
                down_button = constants.button_state["button_up"]

        if keys & ugame.K_LEFT != 0:  # left button possible positions
            if left_button == constants.button_state["button_up"]:
                left_button = constants.button_state["button_just_pressed"]
            elif left_button == constants.button_state["button_just_pressed"]:
                left_button = constants.button_state["button_still_pressed"]
        else:
            if left_button == constants.button_state["button_still_pressed"]:
                left_button = constants.button_state["button_released"]
            else:
                left_button = constants.button_state["button_up"]

        if keys & ugame.K_RIGHT != 0:  # right button possible positions
            if right_button == constants.button_state["button_up"]:
                right_button = constants.button_state["button_just_pressed"]
            elif right_button == constants.button_state["button_just_pressed"]:
                right_button = constants.button_state["button_still_pressed"]
        else:
            if right_button == constants.button_state["button_still_pressed"]:
                right_button = constants.button_state["button_released"]
            else:
                right_button = constants.button_state["button_up"]

        # keys
        if keys & ugame.K_X:  # a
            pass
        if keys & ugame.K_O:  # b
            pass
        if keys & ugame.K_START:  # start
            pass
        if keys & ugame.K_SELECT:  # select
            pass
        if keys & ugame.K_RIGHT != 0:  # right
            if vilheleme.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                vilheleme.move(constants.SCREEN_X - constants.SPRITE_SIZE,
                               vilheleme.y)
            elif right_button == constants.button_state["button_just_pressed"]:
                vilheleme.move(vilheleme.x + constants.SPRITE_SIZE, vilheleme.y)
            else:
                pass

        if keys & ugame.K_LEFT:  # left
            if vilheleme.x < 0:
                vilheleme.move(0, vilheleme.y)
            elif left_button == constants.button_state["button_just_pressed"]:
                vilheleme.move(vilheleme.x - constants.SPRITE_SIZE, vilheleme.y)
            else:
                pass

        if keys & ugame.K_UP:  # up
            if vilheleme.y < 0:
                vilheleme.move(vilheleme.x, 0)
            elif up_button == constants.button_state["button_just_pressed"]:
                vilheleme.move(vilheleme.x, vilheleme.y - constants.SPRITE_SIZE)
            else:
                pass

        if keys & ugame.K_DOWN:  # down
            if vilheleme.y > constants.SCREEN_Y - 8:
                vilheleme.move(vilheleme.x,
                               constants.SCREEN_Y - 8)
            elif down_button == constants.button_state["button_just_pressed"]:
                vilheleme.move(vilheleme.x, vilheleme.y + constants.SPRITE_SIZE)
            else:
                pass

        game.render_sprites(vilheleme_list + water_sprites + ice_sprites + wall_sprites + key_list + door_list + finish_list)
        game.tick()

#        LVL_1()

        def LVL_1():
            # This is level one.

            counter = 0

#            if vilheleme.x < 0:
#                vilheleme.move(32, 32)

#            if wall_sprites[counter].x < 0:
#                wall_sprites[counter].move(16, 16)
#                counter += 1

#        if a_button == constants.button_state["button_just_pressed"]:
#                                            sound.play(lavender_first)


if __name__ == "__main__":
    splash_scene()
