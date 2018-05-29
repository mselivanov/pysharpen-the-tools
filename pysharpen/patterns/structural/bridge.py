"""
Module for demonstrating bridge pattern.
Problem:
1. Parallel or orthogonal hierarchies.
2. One abstract, one - implementation dependent.
"""

class PlasticBottleMaker(object):
    """"""
    def make(self, bottle):
        print("Bottle {0} is made from plastic".format(bottle)) 

class GlassBottleMaker(object):
    """"""
    def make(self, bottle):
        print("Bottle {0} is made from glass".format(bottle)) 

class Bottle(object):
    """Abstract bottle"""    
    def __init__(self, bottle_maker, volume, sticker):
        self._bottle_maker = bottle_maker
        self._sticker = sticker
        self._volume = volume
        
    def __str__(self):
        return "{0} vol. {1}".format(self._sticker, self._volume)
    
    def make(self):
        self._bottle_maker.make(self)
    


def main():
    pm = PlasticBottleMaker()
    gm = GlassBottleMaker()
    b1 = Bottle(pm, 0.5, "Beerbank IPA")
    b2 = Bottle(gm, 0.33, "Beerbank Black IPA")
    b1.make()
    b2.make()

if __name__ == "__main__":
    main()