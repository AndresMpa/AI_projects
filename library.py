import math as mt
import random as rd
import pygame as pg
from basic import constants as cts


# Screen topics

def new_window(title="Title", size=None):
    if size is None:
        size = [cts.width, cts.height]
    pg.display.set_caption(title)
    return pg.display.set_mode(size)


def change_window_name(title):
    pg.display.set_caption(title)


def flip():
    pg.display.flip()


def fill(window, color=cts.BLACK):
    window.fill(color)


def fill_and_flip(window, color=cts.BLACK):
    window.fill(color)
    pg.display.flip()


def frames_per_second_basics():
    return pg.time.Clock()


def frames_per_second(clock, options=2, frames=60):
    if options == 0:
        clock.tick(frames)
    elif options == 1:
        clock.tick(30)
    elif options == 2:
        clock.tick(60)
    elif options == 3:
        clock.tick(120)
    elif options == 4:
        clock.tick(244)
    elif options == 5:
        clock.tick(420)
    elif options == 6:
        clock.tick(620)
    elif options == 7:
        clock.tick(980)
    elif options == 8:
        clock.tick(1080)
    elif options == 9:
        clock.tick(1200)
    elif options == 10:
        clock.tick(1500)
    flip()


def create_color(r=255, g=255, b=255):
    return pg.Color(r, g, b)


def random_color():
    r = int(rd.randint(0, 255))
    g = int(rd.randint(0, 255))
    b = int(rd.randint(0, 255))
    return create_color(r, g, b)


def random_range(start, stop):
    return rd.randrange(start, stop)


def write(txt, size, selected_font=1, colors=cts.WHITE):
    pg.font.init()
    font_1 = pg.font.SysFont("Alba super", size)
    font_2 = pg.font.SysFont("04b, 30", size)
    font_3 = pg.font.SysFont("Admiration Pains", size)
    font_4 = pg.font.SysFont("Otra Mas stf", size)
    if selected_font == 1:
        write_text = font_1.render(txt, 0, colors)
        return write_text
    if selected_font == 2:
        write_text = font_2.render(txt, 0, colors)
        return write_text
    if selected_font == 3:
        write_text = font_3.render(txt, 0, colors)
        return write_text
    if selected_font == 4:
        write_text = font_4.render(txt, 0, colors)
        return write_text


# basic figures

def point(window, coord, color=cts.RED, size=5):
    pg.draw.circle(window, color, coord, size)


def line(window, coord_start, coord_end, color=cts.WHITE, size=3):
    pg.draw.line(window, color, coord_start, coord_end, size)


def triangle(window, axe_1, axe_2, axe_3, color=cts.WHITE, size=3):
    pg.draw.lines(window, color, axe_1, [axe_2, axe_3], size)


def more_figures(window, axe_1, axes, color=cts.WHITE, size=3):
    pg.draw.lines(window, axe_1, axes, color, size)


def polygons(window, points, color=cts.WHITE, size=3):
    pg.draw.polygon(window, color, points, size)


def polygons_filled(window, points, color=cts.WHITE):
    pg.draw.polygon(window, color, points)


# Vectors

def random_position():
    x = rd.randrange(0, (cts.width - 35))
    y = rd.randrange(0, (cts.height - 35))
    return [x, y]
