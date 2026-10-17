"""STUB: effect not implemented — do not guess mechanics.
Rapidash (XY11 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="63a6f5fb-f17a-51c1-8668-eae42c78d97c",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rapidash.Name",
    display_name="Rapidash",
    searchable_by=["Rapidash", "Stage 1", "Rapidash"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard a Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)