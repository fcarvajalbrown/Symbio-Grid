import pygame
import math


_COLOR_LOW = (180, 80, 60)
_COLOR_HIGH = (244, 162, 97)
_CORE = (210, 110, 80)
_N_HYPHAE = 6


def draw_fungi(surface: pygame.Surface, rect: pygame.Rect, agent) -> None:
    t = min(agent.phosphorus / 15.0, 1.0)
    color = _lerp(_COLOR_LOW, _COLOR_HIGH, t)
    cx, cy = rect.centerx, rect.centery
    r = max(rect.width // 2 - 2, 2)
    for i in range(_N_HYPHAE):
        angle = (2 * math.pi * i) / _N_HYPHAE
        ex = int(cx + math.cos(angle) * r)
        ey = int(cy + math.sin(angle) * r)
        pygame.draw.line(surface, color, (cx, cy), (ex, ey), 1)
    pygame.draw.circle(surface, _CORE, (cx, cy), max(r // 4, 1))


def _lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
