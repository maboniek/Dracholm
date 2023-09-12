# Welcome to Dracholm! We have eagerly awaited your visit, stranger..

import tcod

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler

def main():
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    with tcod.context.new_terminal(
        screen_width,
        screen_height,

        tileset = tileset,

        title = "Dracholm: Fires of Ghax",
        vsync = True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            
            for entity in entities:
                root_console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)

            context.present(root_console)
            root_console.clear()
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapeAction):
                    raise SystemExit()
            
if __name__ == "__main__":
    main()