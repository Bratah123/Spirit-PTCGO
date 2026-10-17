"""STUB: effect not implemented — do not guess mechanics.
Manaphy-EX (XY9 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="376194e2-8ffa-59aa-97c9-cf87d13861ce",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ManaphyEX.Name",
    display_name="Manaphy-EX",
    searchable_by=["Manaphy-EX", "Basic", "EX", "ManaphyEX"],
    subtypes=["Basic", "EX"],
    collector_number=32,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Ability(
            title="Aqua Tube",
            game_text="Each of your Pok\u00e9mon that has any Water Energy attached to it has no Retreat Cost.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mineral Pump",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)