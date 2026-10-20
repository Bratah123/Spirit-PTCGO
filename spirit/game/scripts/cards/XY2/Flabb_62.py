"""STUB: effect not implemented — do not guess mechanics.
Flabébé (XY2 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb75c4bc-6b1b-5ec9-ba97-570aac667f95",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    display_name="Flab\u00e9b\u00e9",
    searchable_by=["Flabébé", "Basic", "Flabb"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=669,
    abilities=[
        Attack(
            title="Aromatherapy",
            game_text="Heal 10 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)