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
            "Do you know how to make programs?",
            "Do you like gaming?",
            "What comcept do you like the most?",
            "What kind of machine do you have?"
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
            ),
            (
                ["Yeah, sure! I'm downloding pirate torrents each day!", [aset('win', 5)]],
                ["Yeah, I'm gaming with Steam and licence games only.", []],
                ["No, I use computer strictly for work (maybe little small games sometimes)", [aset('lin', 2), aset('mac', 2)]],
            ),
            (
                ["Everything is FREE and OpenSource. Freedom is cool.", [aset('lin', 3)]],
                ["Everything smooth and well-designed. Art is cool.", [aset('mac', 3)]],
                ["I just want my OS to work out of the box and support popular software. Support is cool.", [aset('win', 3)]],
            ),
            (
                ["Gaming powerful machine.", [aset('win', 3)]],
                ["Mac", [aset('mac', 5)]],
                ["Supercomputer", [aset('lin', 6)]],
                ["Netbook", [aset("lin", 3)]]
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
                "How do you even use Linux when you hate it so much? You're definitely not a Linux user, try to switch to anything else.",
                "Well, you aren't into Linux for sure, although it's your current OS. I'd suggest you try something else.",
                "You use Linux every day? I doubt it. Even though you use it, it seems like something else suits your needs better.",
                "You use Linux and you love it, but not quite passionate and admirable as it's you life choice. You have little intention to switch OS, so try it!",
                "It seems your life choice is right: Linux suits you perfectly. Although, it could suit you better. You can try switching OS if you'd like new experience.",
                "You life choice is perfect indeed! Linux system is the most suitable system for your needs and desires. Don't switch OS unless you definitely need to.",
            ),
            (
                "You seem to hate Linux so much it's even odd coming from a MAC user.",
                "For a MAC user you have strangely little interest in Linux.",
                "You don't need to switch to Linux unless you want to discover advantages over your MAC. It's not for you obviously, although you have a little interest in it.",
                "So you'd like to try Linux. You can try. For a MAC user, it'd be an easy change. You just have to get used to typing into terminal more.",
                "You seem to like Linux very much, although you're MAC user. You want to become a geek? Suit yourself!",
                "Linux is just perfect OS for you. Abandon your f**king MAC! Go suit your needs using the power of Linux.",
            ),
            (
                "You hate Linux almost as passionate as Windows user :)",
                "You have almost none interest in Linux. It's common amidst Windows user who are usually ignorant.",
                "Your little interest in Linux compensated by common Windows software (and games). Am I right? So try installing VirtualBox and trying out some Linux distro.",
                "You have little urge to discover Linux, although not so passionate as other OS. So try it if you want. Just remember: it's not Windows :)",
                "You're surely into Linux. I guess, the only thing that holding you back on Windows is software or games.",
                "You love Linux SO MUCH that you should remove your Windows right NOW and install fresh Arch Linux distro at once :)",
            )]
            macosText = [(
                "You are truly HATE it. You hate it so much that I guess you're messing with your room just to prove you're not MAC user. I guess you're just hardcore GEEK who LOVES console and ASCII.",
                "You have almost none interest in MasOS. You are surely not a designer or video editor, considering you are a Linux user.",
                "MAC is definitely not your choice. Although you're little interested in it.",
                "You should probably at least try MAC. After Linux it'd be an easy change, considering your interest in it.",
                "You are surely would LOVE to use MAC. You have so many hints that you're into it. Try to switch from Linux, it'd worth it.",
                "You LOVE MAC so much that you're even probably going to MAC-donalds just to prove that you're MAC fan. You should definitely switch from Linux, I say you that!",
            ),
            (
                "Why do you use MAC if you HATE it so much? Try to switch to anything else as fast as possible for your own good.",
                "You don't have much intention to use MAC. So try to switch to something else.",
                "MAC's not your choice, but you have some interest in it. Situation is curious cause you're actually a MAC user. I'd recommend you to try out something new.",
                "You like MAC little, but you like it. You may stay with your choice or try to switch to something else.",
                "You are surely LOVE your MAC. But also you are ocnsidering other OS. So try it out if you want but don't get too excited: MAC is best choice for you.",
                "MAC is the most awesome OS you've ever known and you LOVE it. You don't need another OS at all.",
            ),
            (
                "You hate MAC with all your soul. Don't try to use it or else!",
                "You have no interest in MacOS, it's common among Windows users.",
                "You are interested in MAC, but you are not fond of it. Try it over virtualbox first and don't forget: for your needs other OS would be better choice.",
                "MAC is surely intriguing you as Windows user who never saw Unix system. But it's not perfect for your needs, so try it carefully.",
                "You LOVE mac and it suits for your needs pretty good. I suggest you use it as alternative for Windows or as second OS.",
                "You LOVE mac and it PERFECT for your needs. So f*ck Windows! Switch to MAC immediately! I command it!",
            )]         
            windowsText = [(
                "You hate Windows as hell! Don't use it EVER. As Linux user, you are supported.",
                "You have no interest for Windows at all and it doesn't suits your needs. So don't use it unless you forced to.",
                "You have little interest in Windows, and I guess this isn't gonna help you to switch to it because you already using Linux.",
                "You need Windows for your goals or you just like it. But this is little love you have, so you don't need to switch to it instantly.",
                "You LOVE Windows and you need it for your goals. But ALSO you can use another OS, so don't rush with conclusions. Although, Windows would be better choice for you.",
                "You NEED windows HARD. This is the BEST and PERFECT choice for you. So what are you doing with Linux?",
            ),
            (
                "You hate Windows as hell! Don't use it EVER.",
                "You have no interest for Windows at all and it doesn't suits your needs. So don't use it unless you forced to.",
                "You have little interest in Windows, although considering you're MAC user, this is strange. Maybe you just need powerful SCADA or gaming.",
                "You need Windows for your goals or you just like it. But this is little love you have, so you don't need to switch to it instantly.",
                "You LOVE Windows and you need it for your goals. But ALSO you can use another OS, so don't rush with conclusions. Although, Windows would be better choice for you.",
                "You NEED windows HARD. This is the BEST and PERFECT choice for you. So what are you doing with MAC?",
            ),
            (
                "You hate Windows as hell! Why do you use it at all?",
                "You have no interest for Windows at all and it doesn't suits your needs. So switch it off to something else!",
                "You have little interest in Windows, but you are using it as your OS. Are you gamer or student?",
                "You need Windows for your goals and you like it. But this is little love you have, so you can consider switching OS.",
                "You LOVE Windows and you need it for your goals. So you are right about your OS choice. But you can ALSO try another OS if you wish.",
                "Your life choice is right. Windows is the BEST and PERFECT choice for you.",
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
            elif 40 < linux <= 100:
                ltext = linuxText[self.current][5]

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
            elif 40 < macos <= 100:
                mtext = macosText[self.current][5]

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
            elif 40 < windows <= 100:
                wtext = windowsText[self.current][5]

            link = [' Also, ', ' Now, ', ' Well, ', ' So, ', ' Meanwhile ']
            self.finalText = 'Congratulations! You have finished the test. So... ' + ltext + random.choice(link) + mtext + random.choice(link) + wtext

        while True:
            clock.tick(30)

            events = pg.event.get()
            for e in events:
                if e.type == pg.QUIT:
                    quit()
            if self.menu.events(events) == 'Next':
                return

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
