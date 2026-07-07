import pygame
from dataclasses import replace
from symbiogrid.model.config import SimulationConfig, PRESETS

_BG = (13, 13, 13)
_PANEL = (22, 22, 22)
_GREEN = (82, 183, 136)
_AMBER = (244, 162, 97)
_TEXT = (180, 180, 180)
_DIM = (80, 80, 80)
_SEL = (40, 80, 60)


class _Slider:
    def __init__(self, label: str, min_v: float, max_v: float, value: float):
        self.label = label
        self.min = min_v
        self.max = max_v
        self.value = value
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.dragging = False

    def handle(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.dragging = True
            self._set(event.pos[0])
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self._set(event.pos[0])

    def _set(self, mx: int) -> None:
        t = max(0.0, min(1.0, (mx - self.rect.x) / max(self.rect.width, 1)))
        self.value = self.min + t * (self.max - self.min)

    def draw(self, surface: pygame.Surface, font: pygame.font.Font, x: int, y: int, w: int) -> None:
        self.rect = pygame.Rect(x, y + 18, w, 10)
        label = font.render(f"{self.label}  {self.value:.2f}", True, _TEXT)
        surface.blit(label, (x, y))
        pygame.draw.rect(surface, _DIM, self.rect)
        fill_w = int((self.value - self.min) / (self.max - self.min) * w)
        pygame.draw.rect(surface, _GREEN, (x, y + 18, fill_w, 10))


class StartScreen:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        pygame.font.init()
        self._title = pygame.font.SysFont("monospace", 28, bold=True)
        self._font = pygame.font.SysFont("monospace", 14)
        self._small = pygame.font.SysFont("monospace", 12)

        self._preset_keys = list(PRESETS.keys())
        self._preset_idx = 0
        self._grid_options = [(40, 25), (60, 40), (80, 50), (100, 65)]
        self._grid_idx = 1
        self._seed_text = ""
        self._seed_active = False

        p = PRESETS[self._preset_keys[0]]
        self._sliders = {
            "carbon_density":    _Slider("Carbon density",    0.1, 1.0, p.carbon_density),
            "phosphorus_density": _Slider("Phosphorus density", 0.1, 1.0, p.phosphorus_density),
            "mutation_rate":     _Slider("Mutation rate",     0.0, 0.5, p.mutation_rate),
        }
        self._launch_rect = pygame.Rect(0, 0, 0, 0)
        self._preset_rects: list[pygame.Rect] = []
        self._grid_rects: list[pygame.Rect] = []
        self._seed_box_x = 0
        self._seed_box_y = 0

    def handle_events(self, events: list) -> SimulationConfig | None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self._seed_active:
                    if event.key == pygame.K_BACKSPACE:
                        self._seed_text = self._seed_text[:-1]
                    elif event.unicode.isdigit() and len(self._seed_text) < 10:
                        self._seed_text += event.unicode
                if event.key == pygame.K_RETURN:
                    return self._build()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                result = self._handle_click(event.pos)
                if result:
                    return result
            for s in self._sliders.values():
                s.handle(event)
        return None

    def _handle_click(self, pos: tuple) -> SimulationConfig | None:
        for i, r in enumerate(self._preset_rects):
            if r.collidepoint(pos):
                self._preset_idx = i
                self._apply_preset()
                return None
        for i, r in enumerate(self._grid_rects):
            if r.collidepoint(pos):
                self._grid_idx = i
                return None
        seed_rect = pygame.Rect(self._seed_box_x, self._seed_box_y, 160, 24)
        if seed_rect.collidepoint(pos):
            self._seed_active = True
        else:
            self._seed_active = False
        if self._launch_rect.collidepoint(pos):
            return self._build()
        return None

    def _apply_preset(self):
        p = PRESETS[self._preset_keys[self._preset_idx]]
        self._sliders["carbon_density"].value = p.carbon_density
        self._sliders["phosphorus_density"].value = p.phosphorus_density
        self._sliders["mutation_rate"].value = p.mutation_rate

    def _build(self) -> SimulationConfig:
        w, h = self._grid_options[self._grid_idx]
        seed = int(self._seed_text) if self._seed_text else None
        return SimulationConfig(
            width=w, height=h, seed=seed,
            carbon_density=self._sliders["carbon_density"].value,
            phosphorus_density=self._sliders["phosphorus_density"].value,
            mutation_rate=self._sliders["mutation_rate"].value,
        )

    def draw(self) -> None:
        sw, sh = self.surface.get_size()
        self.surface.fill(_BG)

        title = self._title.render("SYMBIO-GRID", True, _GREEN)
        self.surface.blit(title, (sw // 2 - title.get_width() // 2, 30))
        sub = self._small.render("An Evolutionary Mycelial Automaton", True, _DIM)
        self.surface.blit(sub, (sw // 2 - sub.get_width() // 2, 68))

        col_x = sw // 2 - 280
        y = 110
        self._draw_label("PRESET", col_x, y)
        y += 22
        self._preset_rects = []
        for i, key in enumerate(self._preset_keys):
            sel = i == self._preset_idx
            r = pygame.Rect(col_x, y, 200, 26)
            self._preset_rects.append(r)
            pygame.draw.rect(self.surface, _SEL if sel else _PANEL, r, border_radius=3)
            color = _GREEN if sel else _TEXT
            lbl = self._font.render(key, True, color)
            self.surface.blit(lbl, (col_x + 8, y + 5))
            y += 32

        y += 10
        self._draw_label("GRID SIZE", col_x, y)
        y += 22
        self._grid_rects = []
        gx = col_x
        for i, (gw, gh) in enumerate(self._grid_options):
            sel = i == self._grid_idx
            r = pygame.Rect(gx, y, 88, 26)
            self._grid_rects.append(r)
            pygame.draw.rect(self.surface, _SEL if sel else _PANEL, r, border_radius=3)
            lbl = self._font.render(f"{gw}×{gh}", True, _GREEN if sel else _TEXT)
            self.surface.blit(lbl, (gx + 8, y + 5))
            gx += 96

        right_x = sw // 2 + 40
        y = 110
        self._draw_label("PARAMETERS", right_x, y)
        y += 24
        for s in self._sliders.values():
            s.draw(self.surface, self._font, right_x, y, 240)
            y += 46

        y += 10
        self._draw_label("SEED  (blank = random)", right_x, y)
        y += 22
        self._seed_box_x = right_x
        self._seed_box_y = y
        seed_rect = pygame.Rect(right_x, y, 160, 24)
        color = _GREEN if self._seed_active else _DIM
        pygame.draw.rect(self.surface, _PANEL, seed_rect)
        pygame.draw.rect(self.surface, color, seed_rect, 1)
        seed_surf = self._font.render(self._seed_text or "—", True, _TEXT)
        self.surface.blit(seed_surf, (right_x + 6, y + 4))

        btn_y = sh - 70
        btn_w, btn_h = 180, 40
        btn_x = sw // 2 - btn_w // 2
        self._launch_rect = pygame.Rect(btn_x, btn_y, btn_w, btn_h)
        pygame.draw.rect(self.surface, _GREEN, self._launch_rect, border_radius=5)
        lbl = self._font.render("LAUNCH  [Enter]", True, _BG)
        self.surface.blit(lbl, (btn_x + btn_w // 2 - lbl.get_width() // 2, btn_y + 11))

    def _draw_label(self, text: str, x: int, y: int) -> None:
        s = self._small.render(text, True, _DIM)
        self.surface.blit(s, (x, y))
