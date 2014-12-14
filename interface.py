import pygame as pg

class Menu():
    X, Y = 10, 250
    DCOLOR, HCOLOR = (50, 100, 50), (200, 200, 200)
    FONT = pg.font.Font('font.otf', 40)
    SELECT_SOUND = pg.mixer.Sound('Sounds/door.ogg')
    SWITCH_SOUND = pg.mixer.Sound('Sounds/click.ogg')

    out = 150 #for X changing
    selected = 0    #Index of selected menu item
    unselected = 0  #Index of unselected menu (for cool effects)
    now = 0         #Index of menu which is showing NOW
    unsel_timer = 0   #30 for 1 sec --- sel. timer for cool effects
    sel_timer = 0

    def __init__(self, items):
        self.ITEMS = items
        self.update()

    def update(self):
        self.out = 150
        self.selected = 0
        self.unselected = 0
        self.items = [{'Label': i[0], 'Action': i[1]} for i in self.ITEMS]

    def draw(self, surface):
        offset = 0 #Incremental variable for making y-difference

        self.RECT = pg.Rect((0, 0, surface.get_width(), surface.get_height() / 3))
        mysurface = pg.Surface(self.RECT.size, pg.SRCALPHA, 32)
        mysurface.fill((0,0,0, 150))
        surface.blit(mysurface, (0, 240))

        for index, i in enumerate(self.items):
            if self.selected == index:
                if self.sel_timer >= 0:
                    self.sel_timer -= 4
                    color = (self.HCOLOR[0] + int(self.sel_timer*1.5),
                             self.HCOLOR[1],
                             self.HCOLOR[2])
                else:
                    color = self.HCOLOR
            elif self.unselected == index:
                if self.unsel_timer > 1:
                    self.unsel_timer -= 1
                    color = (self.HCOLOR[0] - int(self.HCOLOR[0] / self.unsel_timer),
                             self.HCOLOR[1] - int(self.HCOLOR[1] / self.unsel_timer),
                             self.HCOLOR[2] - int(self.HCOLOR[2] / self.unsel_timer))
                else:
                    color = self.DCOLOR
            else:
                color = self.DCOLOR
            text = self.FONT.render(i['Label'], True, color)
            if self.out > 0:
                surface.blit(text, (self.X-self.out, self.Y + offset))
                self.out -= 10
            else:
                surface.blit(text, (self.X, self.Y + offset))
            offset += self.FONT.get_height()

    def events(self, events):
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_DOWN or e.key == pg.K_j or e.key == pg.K_s:
                    if self.selected < len(self.items) - 1:
                        self.SWITCH_SOUND.play()
                        self.unselected = self.selected
                        self.selected += 1
                        self.unsel_timer = 10
                        self.sel_timer = 40
                elif e.key == pg.K_UP or e.key == pg.K_k or e.key == pg.K_w:
                    if self.selected > 0:
                        self.SWITCH_SOUND.play()
                        self.unselected = self.selected
                        self.selected -= 1
                        self.unsel_timer = 10
                        self.sel_timer = 40
                elif e.key == pg.K_RETURN or e.key == pg.K_SPACE or e.key == pg.K_l:
                    self.SELECT_SOUND.play()
                    for item in self.items[self.selected]['Action']:
                        item()
                    return 'Next'
                    #self.update()

class Message():
    ALPHA = 130
    hidden = False
    hid_timer = 500;
    FONT_COLOR = (200,200,200)
    HEIGHT = 220

    def __init__(self, surface):
        self.RECT = pg.Rect((0, 0, surface.get_size()[0] - 10*2, self.HEIGHT))
        self.X = surface.get_size()[0] / 2 - self.RECT.width / 2
        self.setFontSize(30)
        self.surface = surface

    def setFontSize(self, size):
        self.FONT = pg.font.Font('font.otf', size)

    def wordwrap(self, text):
        size = 20

        finallines = []
        lines = text.splitlines()
        for line in lines:
            if self.FONT.size(line)[0] > self.RECT.width:
                words = line.split(' ')
                newline = ''
                for word in words:
                    while self.FONT.size(word)[0] >= self.RECT.width:
                        size -= 1
                        self.setFontSize(size)
                    testline = newline + word + ' '
                    if self.FONT.size(testline)[0] < self.RECT.width:
                        newline = testline
                    else:
                        finallines.append(newline)
                        newline = word + ' '
                finallines.append(newline)
            else:
                finallines.append(line)

        return finallines

    def draw(self, finallines):
        if self.hidden == False or (self.hidden == True and self.hid_timer < 1000):
            surface = pg.Surface(self.RECT.size, pg.SRCALPHA, 32)
            surface.fill((0,0,0, self.ALPHA))

            height = 0
            for line in self.wordwrap(finallines):
                text = self.FONT.render(line, True, self.FONT_COLOR)
                surface.blit(text, ((self.RECT.width - text.get_width()) / 2, height))
                height += self.FONT.size(line)[1]

            self.surface.blit(surface, (self.X - self.hid_timer, 10))
            if self.hidden == False and self.hid_timer > 0:
                self.hid_timer -=100
            elif self.hidden == True:
                self.hid_timer +=100
