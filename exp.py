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
            "It is known that overall look of the room is a great indicator of personality. So, describe your room.",
            "What application do you expect to use the most?",
            "Do you know how to make programs?"
        )
        self.items = (
            (
                ['I need another OS', []],
                ["I don't need another OS", [lambda: quit()]]
            ),
            (
                ['Linux', [aset('current', 0)]],
                ['MacOS', [aset('current', 1), aset('step', 2)]],
                ['Windows', [aset('current', 2), aset('step', 3)]],
                ['BSD', [aset('current', 0), aset('step', 4)]]
            ),
            (
                ['I am a geek', [aset('step', 5), aset('lin', 5)]],
                ["I'm just regular ubuntu user, I like fancy windows and glowing buttons", [aset('step', 5), aset('mac', 2)]],
                ['Neither. I am advanced user using linux for server purposes or other means', [aset('step', 5), aset('lin', 2)]]
            ),
            (
                ["I'm bored with perfectness. Need something raw.", [aset('step', 5), aset('win', 3), aset('lin', 1)]],
                ["I love my MAC. I just curious about test results.", [aset('step', 5), aset('mac', 2)]],
                ['I am displeased about MAC and need something more perfect', [aset('step', 5), aset('mac', -4)]]
            ),
            (
                ["I don't like viruses, system errors and slow loading", [aset('step', 5), aset('lin', 4), aset('mac', 1), aset('win', -2)]],
                ["I don't like OS design. Everything else is perfect.", [aset('step', 5), aset('mac', 3)]],
                ['I like Windows. Just curious about Unix.', [aset('step', 5), aset('win', 3), aset('lin', 1)]]
            ),
            (
                ["Okay", [lambda: quit()]],
                ["Hell no! I'm gonna continue cause I'm super cool BSD Man!", [aset('step', 5), aset('lin', 1)]]
            ),
            (
                ["It's really messy just like on this photo, I just too lazy to clean up", [aset('lin', 1), aset('mac', -2), aset('win', 3)]],
                ["It is messy just on the table, and I can find anything I want. It is 'creative' mess", [aset('lin', 4), aset('win', 1)]],
                ['It is really clean. All is just perfect.', [aset('mac', 5)]]
            ),
            (
                ["Simple office software", [aset('lin', 2), aset('mac', 3), aset('win', 4)]],
                ["Powerful calculation and science programs: data maintenance, programming", [aset('lin', 4), aset('win', 2)]],
                ['SCADA programs and powerful engineering paid software', [aset('win', 5), aset('lin', -3)]],
                ['Video editing software', [aset('win', 4), aset('mac', 6), aset('lin', -2)]],
                ['Server or supercomputer claster', [aset('lin', 6)]]
            ),
            (
                ["Of course!", [aset('lin', 5), aset('mac', 3)]],
                ["Eeeh... I wrote some basic Hello World programs on BASIC", [aset('win', 3), aset('lin', 2)]],
                ["Nope, I just wanna gaming", [aset('win', 5)]],
            )

        )
        self.message = interface.Message(surface)

    def loop(self): #settings is settings object (current state already, save-loaded outside, in game.py file)
        clock = pg.time.Clock()
        if self.step != 100:
            self.menu = interface.Menu(self.items[self.step])
            self.BG = pg.transform.scale(pg.image.load('Images/' + str(self.step) + '.jpg'), SIZE)
        else:
            self.menu = interface.Menu((
                ["Okay", [lambda: quit()]],
                ["Quit", [lambda: quit()]]
            ))
            self.BG = pg.transform.scale(pg.image.load('Images/final.jpg'), SIZE)
            #CONDITION based on "lin", "win" and "mac" + "current"
            summary = self.lin + self.mac + self.win
            linux = self.lin * 100 / (summary)
            macos = self.mac * 100 / (summary)
            windows = self.win * 100 / (summary)
            linuxText = [(
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            ),
            (
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            ),
            (
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            )]
            macosText = [(
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            ),
            (
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            ),
            (
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            )]         
            windowsText = [(
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            ),
            (
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            ),
            (
                "zero",
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth"
            )]
            if linux <= 0:
                ltext = linuxText[self.current][0]
            elif 0 < linux <= 10:
                ltext = linuxText[self.current][1]
            elif 10 < linux <= 20:
                ltext = linuxText[self.current][2]
            elif 20 < linux <= 30:
                ltext = linuxText[self.current][3]
            elif 30 < linux <= 40:
                ltext = linuxText[self.current][4]
            elif 40 < linux <= 50:
                ltext = linuxText[self.current][5]
            elif 50 < linux <= 100:
                ltext = linuxText[self.current][6]

            if macos <= 0:
                mtext = macosText[self.current][0]
            elif 0 < macos <= 10:
                mtext = macosText[self.current][1]
            elif 10 < macos <= 20:
                mtext = macosText[self.current][2]
            elif 20 < macos <= 30:
                mtext = macosText[self.current][3]
            elif 30 < macos <= 40:
                mtext = macosText[self.current][4]
            elif 40 < macos <= 50:
                mtext = macosText[self.current][5]
            elif 50 < macos <= 100:
                mtext = macosText[self.current][6]

            if windows <= 0:
                wtext = windowsText[self.current][0]
            elif 0 < windows <= 10:
                wtext = windowsText[self.current][1]
            elif 10 < windows <= 20:
                wtext = windowsText[self.current][2]
            elif 20 < windows <= 30:
                wtext = windowsText[self.current][3]
            elif 30 < windows <= 40:
                wtext = windowsText[self.current][4]
            elif 40 < windows <= 50:
                wtext = windowsText[self.current][5]
            elif 50 < windows <= 100:
                wtext = windowsText[self.current][6]

            self.finalText = 'Congratulations! You have finished the test. So... ' + ltext + mtext + wtext

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
            if self.step != 100:
                self.message.draw(self.text[self.step])
            else:
                self.message.draw(self.finalText)

            pg.display.flip()

if __name__ == '__main__':
    pg.display.set_caption(CAPTION)
    screen = pg.display.set_mode(SIZE)
    menuScreen = Menu(screen)
    while True:
        menuScreen.loop()
        menuScreen.step += 1
        if menuScreen.step == len(menuScreen.text):
            break
    menuScreen.step = 100
    menuScreen.loop()
    pg.quit()
