from tcod import Console
from entity import Entity

class UIhandler:
    def __init__(self, entity: Entity, console: Console):
        self.entity = entity
    
    def render(self, console: Console):
        console.print(1, 78, "Health:"+str(self.entity.health))
        console.print(1, 79, "Gideons:"+str(self.entity.money))
