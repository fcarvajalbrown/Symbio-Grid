from dataclasses import dataclass
from typing import Optional


@dataclass
class SimulationConfig:
    width: int = 60
    height: int = 40
    seed: Optional[int] = None
    n_plants: int = 80
    n_fungi: int = 60
    carbon_density: float = 0.6
    phosphorus_density: float = 0.5
    mutation_rate: float = 0.1
    phosphorus_regen: float = 0.05  # soil phosphorus recovered per cell per tick
    fungi_uptake: float = 1.2  # max soil phosphorus a fungus draws from its neighborhood per tick
    plant_p_decay: float = 0.15  # phosphorus a plant consumes per tick
    fungi_c_decay: float = 0.1  # carbon a fungus consumes per tick
    tick_rate: int = 10  # simulation steps per second
    cell_size: int = 16  # pixels per grid cell


PRESETS = {
    "Sparse Forest": SimulationConfig(
        n_plants=50, n_fungi=25,
        carbon_density=0.4, phosphorus_density=0.3,
        mutation_rate=0.05,
    ),
    "Dense Bloom": SimulationConfig(
        n_plants=140, n_fungi=110,
        carbon_density=0.8, phosphorus_density=0.7,
        mutation_rate=0.1,
    ),
    "Climate Shock": SimulationConfig(
        n_plants=80, n_fungi=60,
        carbon_density=0.5, phosphorus_density=0.15,
        mutation_rate=0.35,
    ),
    "Random": SimulationConfig(),
}
