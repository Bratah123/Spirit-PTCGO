"""STUB: effect not implemented — do not guess mechanics.
Venusaur-EX (XY12 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="422367f7-a694-50b0-b15e-06abb0bcc56d",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name",
    display_name="Venusaur-EX",
    searchable_by=["Venusaur-EX", "Basic", "EX", "VenusaurEX"],
    subtypes=["Basic", "EX"],
    collector_number=1,
    set_code="XY12",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    family_id=3,
    abilities=[
        Attack(
            title="Poison Powder",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Jungle Hammer",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)