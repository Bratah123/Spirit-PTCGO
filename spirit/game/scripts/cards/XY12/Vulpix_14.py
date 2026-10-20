"""STUB: effect not implemented — do not guess mechanics.
Vulpix (XY12 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="33371b9b-a2d1-53d0-9b30-03d7e222318f",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic", "Vulpix"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="XY12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)