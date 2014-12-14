#!/usr/bin/env python3
#Expert System, Ewancoder, 2014

import os
import random

import pygame as pg
pg.mixer.pre_init(44100, -16, 2, 2048)
pg.init()

import interface

CAPTION = 'Expert System "Best Operation System Choice"'
SIZE = (1366,768)

class Menu():
    MUSIC = pg.mixer.Sound('music.ogg')
    step = 0

    current = '' #Your current OS

    win = 0 #Windows points
    mac = 0 #MacOS points
    lin = 0 #Linux points
    bsd = 0 #BSD

    def __init__(self, surface):
        def aset(attr, value):
            if attr not in ('current', 'step'):
                return lambda: setattr(self, attr, getattr(self, attr) + value)
            else:
                return lambda: setattr(self, attr, value)

        self.surface = surface
        self.text = (
            "Greetings! Do you want to switch to another OS? Or maybe you need to find out what best suits your needs?",
            "Okay then. What is your current operation system? If you have multiple OS, choose the one you spend more time with.",
            "So, you're geek? Hacking nets from your terminal? Or are you just regular ubuntu user trying to look cool in the eyes of your colleagues?",
            "So, you like beauty. Beauty of design, hardware and software. And you're not the poor guy. Why do you need to switch OS?",
            "Hah, I knew you'd be a Windows user. Why else you would try to switch OS? Anyway, without jokes, what don't you like about Windows?",
            "Oh, you're tough! You're real serious man, dude! I don't wanna trouble... So quit this test, there's no place for you here. You're already ZEN.",
            "Now that we discovered that currently you prefer " + self.current + ", let's discuss common questions. It is known that overall look of the room is a great indicator of personality. So, describe your room.",
            "What application do you expect to use the most?"
        )
        self.items = (
            (
                ['Yes', []],
                ['No', lambda: quit()]
            ),
            (
                ['Linux', [aset('current', 'lin')]],
                ['MacOS', [aset('current', 'mac'), aset('step', 2)]],
                ['Windows', [aset('current', 'win'), aset('step', 3)]],
                ['BSD', [aset('current', 'bsd'), aset('step', 4)]]
            ),
            (
                ['I am geek', [aset('step', 5), aset('lin', 5)]],
                ["I'm just regular ubuntu user", [aset('step', 5)]],
                ['Neither. I am advanced user using linux for server purposes or other means', [aset('step', 5), aset('lin', 2)]]
            ),
            (
                ["I'm bored with perfectness. Need something raw.", [aset('step', 5), aset('win', 3)]],
                ["I love my MAC. I just curious about test results.", [aset('step', 5), aset('mac', 2)]],
                ['I am displeased about MAC and need something more perfect', [aset('step', 5), aset('mac', -2)]]
            ),
            (
                ["I don't like viruses, system errors and slow loading", [aset('step', 5), aset('lin', 4), aset('mac', 1), aset('win', -2)]],
                ["I don't like OS design. Everything else is perfect.", [aset('step', 5), aset('mac', 2)]],
                ['I like Windows. Just curious about Unix.', [aset('step', 5), aset('win', 3)]]
            ),
            (
                ["Okay", lambda: quit()],
                ["Hell no! I'm gonna continue cause I'm super cool BSD Man!", [aset('step', 5), aset('bsd', 5)]]
            ),
            (
                ["It's really messy just like on this photo, I just too lazy to clean up", [aset('lin', 1), aset('mac', -4), aset('win', 3)]],
                ["It is messy just on the table, and I can find anything I want. It is 'creative' mess", [aset('lin', 4), aset('win', 1)]],
                ['It is really clean. All is just perfect.', [aset('mac', 5), aset('win', -1)]]
            ),
            (
                ["Simple office software", [aset('lin', 3), aset('mac', 2), aset('win', 4)]],
                ["Powerful calculation and science programs: data maintenance", [aset('lin', 4), aset('win', 2)]],
                ['SCADA programs and powerful engineering paid software', [aset('win', 5)]],
                ['Video editing software', [aset('win', 4), aset('mac', 6)]]
            ),
        )
        self.message = interface.Message(surface)

    def loop(self): #settings is settings object (current state already, save-loaded outside, in game.py file)
        clock = pg.time.Clock()
        self.menu = interface.Menu(self.items[self.step])
        self.BG = pg.transform.scale(pg.image.load('Images/' + str(self.step) + '.jpg'), SIZE)

        while True:
            clock.tick(30)

            events = pg.event.get()
            for e in events:
                if e.type == pg.QUIT:
                    quit()
            if self.menu.events(events) == 'Next':
                return

            if not pg.mixer.get_busy():
                self.MUSIC.play(-1)

            self.surface.fill(0)
            self.surface.blit(self.BG, (0, 0))
            self.menu.draw(self.surface)
            self.message.draw(self.text[self.step])

            pg.display.flip()

if __name__ == '__main__':
    pg.display.set_caption(CAPTION)
    screen = pg.display.set_mode(SIZE)
    menuScreen = Menu(screen)
    while True:
        menuScreen.loop()
        menuScreen.step += 1
        if menuScreen.step == 10:
            break
    pg.quit()
