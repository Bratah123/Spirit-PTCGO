from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import search_attach_energy

from spirit.game.card_effects.sm10 import (
    hail_prison,
)

def _is_water_energy(card):
    return energy_provides_type(card, PokemonTypes.WATER.value)

card = PokemonCardDef(
    guid="a3d4a1d7-629a-56ad-9a17-763a81d48713",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name",
    display_name="Kyurem",
    searchable_by=["Kyurem", "Basic", "Kyurem"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Call Forth Cold",
            game_text="Search your deck for a Water Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_attach_energy(predicate=_is_water_energy, count=1, to_self=True),
        ),
        Attack(
            title="Hail Prison",
            game_text="Discard 2 Water Energy from this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=hail_prison
        ),
    ],
)