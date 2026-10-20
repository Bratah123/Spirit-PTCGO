"""STUB: effect not implemented — do not guess mechanics.
M Diancie-EX (Promo_XY #XY44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95586126-4fb8-5120-b2f9-fdd654e1e119",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MDiancieEX.Name",
    display_name="M Diancie-EX",
    searchable_by=["M Diancie-EX", "MEGA", "EX", "MDiancieEX"],
    subtypes=["MEGA", "EX"],
    collector_number=44,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DiancieEX.Name",
    family_id=719,
    abilities=[
        Attack(
            title="Diamond Force",
            game_text="During your opponent's next turn, prevent all damage done to each of your Pok\u00e9mon from your opponent's Pok\u00e9mon-EX. (If this Pok\u00e9mon is no longer your Active Pok\u00e9mon, this effect ends.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)