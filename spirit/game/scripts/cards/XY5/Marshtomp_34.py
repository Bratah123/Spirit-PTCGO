"""STUB: effect not implemented — do not guess mechanics.
Marshtomp (XY5 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc5a4cb1-7368-5107-998e-fb77cb561ad3",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    display_name="Marshtomp",
    searchable_by=["Marshtomp", "Stage 1", "Marshtomp"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    family_id=258,
    abilities=[
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Endeavor",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)