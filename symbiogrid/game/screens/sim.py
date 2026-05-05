import pygame
from symbiogrid.model.model import SymbioModel
from symbiogrid.model.config import SimulationConfig
from symbiogrid.game.renderer import Renderer
from symbiogrid.game.hud import HUD

_SPEED_STEPS = [1, 2, 5, 10, 20, 30]


class SimScreen:
    def __init__(self, surface: pygame.Surface, config: SimulationConfig):
        self.surface = surface
        self.config = config
        self.model = SymbioModel(config)
        self.renderer = Renderer(config)
        self.hud = HUD()
        self.paused = False
        self._speed_idx = _SPEED_STEPS.index(config.tick_rate) if config.tick_rate in _SPEED_STEPS else 3
        self._tick_acc = 0
        self._last_ms = pygame.time.get_ticks()
        self._offset = [0, 0]
        self._dragging = False
        self._drag_origin = (0, 0)
        self._state = self.model.get_state()

    @property
    def _tick_rate(self) -> int:
        return _SPEED_STEPS[self._speed_idx]

    @property
    def _ms_per_tick(self) -> int:
        return 1000 // self._tick_rate

    def handle_events(self, events: list) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                self._handle_key(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._dragging = True
                    self._drag_origin = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self._dragging = False
            elif event.type == pygame.MOUSEMOTION and self._dragging:
                dx = event.pos[0] - self._drag_origin[0]
                dy = event.pos[1] - self._drag_origin[1]
                self._clamp_offset(-dx, -dy)
                self._drag_origin = event.pos
            elif event.type == pygame.MOUSEWHEEL:
                self._clamp_offset(-event.x * 20, -event.y * 20)

    def _handle_key(self, key: int) -> None:
        if key == pygame.K_SPACE:
            self.paused = not self.paused
        elif key == pygame.K_RIGHT or key == pygame.K_EQUALS:
            self._speed_idx = min(self._speed_idx + 1, len(_SPEED_STEPS) - 1)
        elif key == pygame.K_LEFT or key == pygame.K_MINUS:
            self._speed_idx = max(self._speed_idx - 1, 0)
        elif key == pygame.K_UP:
            self._clamp_offset(0, -30)
        elif key == pygame.K_DOWN:
            self._clamp_offset(0, 30)
        elif key == pygame.K_a:
            self._clamp_offset(-30, 0)
        elif key == pygame.K_d:
            self._clamp_offset(30, 0)
        elif key == pygame.K_HOME:
            self._offset = [0, 0]

    def _clamp_offset(self, dx: int, dy: int) -> None:
        gw, gh = self.renderer.grid_pixel_size()
        sw, sh = self.surface.get_size()
        max_x = max(gw - sw, 0)
        max_y = max(gh - sh, 0)
        self._offset[0] = max(0, min(self._offset[0] + dx, max_x))
        self._offset[1] = max(0, min(self._offset[1] + dy, max_y))

    def update(self) -> None:
        if self.paused:
            return
        now = pygame.time.get_ticks()
        self._tick_acc += now - self._last_ms
        self._last_ms = now
        while self._tick_acc >= self._ms_per_tick:
            self.model.step()
            self._tick_acc -= self._ms_per_tick
        self._state = self.model.get_state()

    def draw(self) -> None:
        self.update()
        top = self.hud.bar_height
        bot = self.hud.bar_height
        self.renderer.draw(self.surface, self._state, self._offset, top, bot)
        self.hud.draw_top(self.surface, self._state, self.paused, self._tick_rate)
        self.hud.draw_bottom(self.surface, self._state)
