"""STUB: effect not implemented — do not guess mechanics.
Mew-EX (Promo_XY #XY126): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb8ee538-8659-505f-993f-f5339c2946e6",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewEX.Name",
    display_name="Mew-EX",
    searchable_by=["Mew-EX", "Basic", "EX", "MewEX"],
    subtypes=["Basic", "EX"],
    collector_number=126,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Versatile",
            game_text="This Pok\u00e9mon can use the attacks of any Pok\u00e9mon in play (both yours and your opponent's). (You still need the necessary Energy to use each attack.)",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Replace",
            game_text="Move as many Energy attached to your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)