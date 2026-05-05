import pygame

_BAR_H = 28
_BG = (18, 18, 18)
_TEXT = (180, 180, 180)
_GREEN = (82, 183, 136)
_AMBER = (244, 162, 97)


class HUD:
    def __init__(self):
        pygame.font.init()
        self._font = pygame.font.SysFont("monospace", 13)

    def draw_top(self, surface: pygame.Surface, state: dict, paused: bool, tick_rate: int) -> None:
        w = surface.get_width()
        bar = pygame.Surface((w, _BAR_H))
        bar.fill(_BG)
        self._blit(bar, f"GEN  {state['generation']}", _GREEN, 10)
        speed = self._render(f"{tick_rate} t/s", _TEXT)
        bar.blit(speed, (w // 2 - speed.get_width() // 2, 7))
        status = "PAUSED" if paused else "RUNNING"
        self._blit(bar, status, _TEXT, w, right=True)
        surface.blit(bar, (0, 0))

    def draw_bottom(self, surface: pygame.Surface, state: dict) -> None:
        w, h = surface.get_width(), surface.get_height()
        bar = pygame.Surface((w, _BAR_H))
        bar.fill(_BG)
        ratio = state["n_plants"] / max(state["n_fungi"], 1)
        self._blit(bar, f"Plants  {state['n_plants']}", _GREEN, 10)
        self._blit(bar, f"Fungi  {state['n_fungi']}", _AMBER, w // 3)
        self._blit(bar, f"P/F  {ratio:.2f}", _TEXT, w * 2 // 3)
        self._blit(bar, f"C avg  {state['avg_carbon']:.1f}", _TEXT, w - 110, right=False)
        surface.blit(bar, (0, h - _BAR_H))

    def _render(self, text: str, color: tuple) -> pygame.Surface:
        return self._font.render(text, True, color)

    def _blit(self, surface, text, color, x, right=False):
        s = self._render(text, color)
        bx = x - s.get_width() - 10 if right else x
        surface.blit(s, (bx, 7))

    @property
    def bar_height(self) -> int:
        return _BAR_H
