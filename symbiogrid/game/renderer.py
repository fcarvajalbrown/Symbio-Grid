import pygame
import numpy as np
from symbiogrid.model.config import SimulationConfig
from symbiogrid.model.agents.plant import PlantAgent
from symbiogrid.model.agents.fungi import FungiAgent
from symbiogrid.game.sprites.plant import draw_plant
from symbiogrid.game.sprites.fungi import draw_fungi

_BG = (13, 13, 13)
_P_LOW = (15, 15, 28)
_P_HIGH = (35, 35, 75)


class Renderer:
    def __init__(self, config: SimulationConfig):
        self.config = config
        self.cell = config.cell_size

    def draw(self, surface: pygame.Surface, state: dict, offset: list[int], top: int, bot: int) -> None:
        surface.fill(_BG)
        self._draw_phosphorus(surface, state["phosphorus_map"], offset, top)
        self._draw_agents(surface, state["agents"], offset, top)

    def _draw_phosphorus(self, surface, p_map, offset, top):
        for x in range(self.config.width):
            for y in range(self.config.height):
                level = float(np.clip(p_map[x, y] / 10.0, 0, 1))
                color = _lerp(_P_LOW, _P_HIGH, level)
                rect = self._rect(x, y, offset, top)
                if self._visible(rect, surface):
                    pygame.draw.rect(surface, color, rect)

    def _draw_agents(self, surface, agents, offset, top):
        for agent in agents:
            if agent.pos is None:
                continue
            rect = self._rect(agent.pos[0], agent.pos[1], offset, top)
            if not self._visible(rect, surface):
                continue
            if isinstance(agent, PlantAgent):
                draw_plant(surface, rect, agent)
            elif isinstance(agent, FungiAgent):
                draw_fungi(surface, rect, agent)

    def _rect(self, x, y, offset, top) -> pygame.Rect:
        px = x * self.cell - offset[0]
        py = y * self.cell - offset[1] + top
        return pygame.Rect(px, py, self.cell, self.cell)

    def _visible(self, rect: pygame.Rect, surface: pygame.Surface) -> bool:
        w, h = surface.get_size()
        return rect.right > 0 and rect.left < w and rect.bottom > 0 and rect.top < h

    def grid_pixel_size(self) -> tuple[int, int]:
        return self.config.width * self.cell, self.config.height * self.cell


def _lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
