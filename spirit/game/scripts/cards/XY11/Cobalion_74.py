"""STUB: effect not implemented — do not guess mechanics.
Cobalion (XY11 #74): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84d6522b-651b-5a8a-99ad-1eade3614bb2",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion", "Basic", "Cobalion"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=638,
    abilities=[
        Attack(
            title="Quick Guard",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon during your opponent's next turn. This Pok\u00e9mon can't use Quick Guard during your next turn.",
            cost={PokemonTypes.METAL: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.METAL: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)