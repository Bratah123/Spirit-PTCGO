"""STUB: effect not implemented — do not guess mechanics.
Mantine (XY11 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f42b244-b2e3-5479-8b77-6a02091f15e7",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=226,
    abilities=[
        Attack(
            title="Healing Wave",
            game_text="Discard as many cards as you like from your hand. Heal 10 damage from this Pok\u00e9mon for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dwindling Wave",
            game_text="This attack does 90 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3},
            damage=90,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)