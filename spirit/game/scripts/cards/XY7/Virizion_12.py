"""STUB: effect not implemented — do not guess mechanics.
Virizion (XY7 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cebc353-5dd1-5d65-84ac-c75fd8705fef",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion", "Basic", "Virizion"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Attack(
            title="Bail Out",
            game_text="Put 2 Pok\u00e9mon from your discard pile into your hand.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Prize Count",
            game_text="If you have more Prize cards left than your opponent, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)