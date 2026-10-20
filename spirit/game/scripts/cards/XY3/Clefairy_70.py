"""STUB: effect not implemented — do not guess mechanics.
Clefairy (XY3 #70): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a2bb426e-d476-53b8-8ae2-993bf44a029d",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=35,
    abilities=[
        Attack(
            title="Moonblast",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 10 (before applying Weakness and Resistance).",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)