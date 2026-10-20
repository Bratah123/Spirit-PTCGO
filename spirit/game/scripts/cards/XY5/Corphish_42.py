"""STUB: effect not implemented — do not guess mechanics.
Corphish (XY5 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="453985cd-24ac-52b8-b409-4741b3ae535b",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    display_name="Corphish",
    searchable_by=["Corphish", "Basic", "Corphish"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=341,
    abilities=[
        Attack(
            title="Vice Grip",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)