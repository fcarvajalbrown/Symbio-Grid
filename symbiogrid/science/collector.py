import mesa
from symbiogrid.model.agents.plant import PlantAgent
from symbiogrid.model.agents.fungi import FungiAgent


def _plants(model):
    return [a for a in model.agents if isinstance(a, PlantAgent)]


def _fungi(model):
    return [a for a in model.agents if isinstance(a, FungiAgent)]


def _avg(values):
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def _expressed_trade(model):
    agents = list(model.agents)
    return sum(1 for a in agents if a.intention == "TRADE") / len(agents) if agents else 0.0


def build_collector() -> mesa.DataCollector:
    return mesa.DataCollector(
        model_reporters={
            "generation": lambda m: m.generation,
            "n_plants": lambda m: len(_plants(m)),
            "n_fungi": lambda m: len(_fungi(m)),
            "avg_plant_carbon": lambda m: _avg(a.carbon for a in _plants(m)),
            "avg_plant_phosphorus": lambda m: _avg(a.phosphorus for a in _plants(m)),
            "avg_fungi_carbon": lambda m: _avg(a.carbon for a in _fungi(m)),
            "avg_fungi_phosphorus": lambda m: _avg(a.phosphorus for a in _fungi(m)),
            "soil_phosphorus": lambda m: float(m.phosphorus_map.sum()),
            "expressed_trade": _expressed_trade,
        }
    )


def agent_dna(model) -> list[dict]:
    rows = []
    for a in model.agents:
        rows.append({
            "agent_id": a.unique_id,
            "species": type(a).__name__,
            "carbon": round(a.carbon, 6),
            "phosphorus": round(a.phosphorus, 6),
            "rule_table": a.rule_table.to_bitstring(),
        })
    return rows
