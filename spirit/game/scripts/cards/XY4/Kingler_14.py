"""STUB: effect not implemented — do not guess mechanics.
Kingler (XY4 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa28f6e4-b3d4-5b24-86ae-f5030b61b976",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name",
    display_name="Kingler",
    searchable_by=["Kingler", "Stage 1", "Kingler"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    family_id=98,
    abilities=[
        Attack(
            title="Guard Claw",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.WATER: 4},
            damage=100,
        ),
    ],
)