"""
Module demonstrates facade pattern.
Problem:
1. Reduce complexity for client.
2. Reduce coupling.
"""
class Cow:
    def __init__(self, name, mass):
        self._name = name
        self._mass = mass
    
    def __str__(self):
        return "Cow {0} weighs {1}".format(self._name, self._mass)

class Chair:        
    def __init__(self, material):
        self._material = material
    
    def __str__(self):
        return "{0} chair".format(self._material)
        
class NonLivingMatterBreaker(object):
    
    def break_object(self, obj):
        print("Breaking {0} into atoms".format(obj))

class NonLivingMatterComposer(object):
    
    def compose_object(self, obj):
        print("Composing {0} from atoms".format(obj))

class LivingMatterBreaker(object):
    
    def break_creature(self, creature):
        print("Breaking carefully {0} into atoms".format(creature))

class LivingMatterComposer(object):
    
    def compose_creature(self, creature):
        print("Composing carefully {0} from atoms".format(creature))


class TeleporterFacade(object):
    def __init__(self, nlm_breaker, nlm_composer, lc_breaker, lc_composer):
        self._nlm_breaker = nlm_breaker
        self._nlm_composer = nlm_composer
        self._lc_breaker = lc_breaker
        self._lc_composer = lc_composer
        
    def teleport(self, objects, creatures):    
        for obj in objects:
            self._nlm_breaker.break_object(obj)
            self._nlm_composer.compose_object(obj)            
        for creature in creatures:
            self._lc_breaker.break_creature(creature)            
            self._lc_composer.compose_creature(creature)
        

def main():
    t = TeleporterFacade(NonLivingMatterBreaker(), NonLivingMatterComposer(), LivingMatterBreaker(), LivingMatterComposer())
    t.teleport([Chair("Wooden")], [Cow("Dolly", "120 kg")])

if __name__ == "__main__":
    main()