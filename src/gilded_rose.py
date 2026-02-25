# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def set_sellin(self):
        self.sell_in -= 1

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
class Updateable:
    def update_quality(self):
        pass

class NormalItem(Item, Updateable):

    Item.set_sellin

    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        elif self.sell_in < 0:
            self.quality -= 2

class AgedBrie(Item, Updateable):

    Item.set_sellin

    def update_quality(self):
        if self.sell_in > 0:
            self.quality += 1
        elif self.sell_in < 0:
            self.quality +=2