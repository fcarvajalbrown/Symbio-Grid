import sys
import pygame
from symbiogrid.game.screens.start import StartScreen
from symbiogrid.game.screens.sim import SimScreen


def run() -> None:
    pygame.init()
    surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    pygame.display.set_caption("Symbio-Grid")
    clock = pygame.time.Clock()

    screen: StartScreen | SimScreen = StartScreen(surface)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode(event.size, pygame.RESIZABLE)

        if isinstance(screen, StartScreen):
            config = screen.handle_events(events)
            if config is not None:
                screen = SimScreen(surface, config)
            screen.draw()
        else:
            screen.handle_events(events)
            screen.draw()

        pygame.display.flip()
        clock.tick(60)
