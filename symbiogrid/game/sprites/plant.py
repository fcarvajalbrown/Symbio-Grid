import pygame


_COLOR_LOW = (45, 106, 79)
_COLOR_HIGH = (82, 183, 136)
_STEM = (34, 85, 60)


def draw_plant(surface: pygame.Surface, rect: pygame.Rect, agent) -> None:
    t = min(agent.carbon / 15.0, 1.0)
    color = _lerp(_COLOR_LOW, _COLOR_HIGH, t)
    cx, cy = rect.centerx, rect.centery
    r = max(rect.width // 2 - 2, 2)
    stem_top = cy - r // 2
    pygame.draw.line(surface, _STEM, (cx, cy + r), (cx, stem_top), max(rect.width // 6, 1))
    pygame.draw.circle(surface, color, (cx, stem_top - r // 3), r // 2 + 1)


def _lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
