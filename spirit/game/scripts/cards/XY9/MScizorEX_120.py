"""STUB: effect not implemented — do not guess mechanics.
M Scizor-EX (XY9 #120): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7f940ad9-d5e3-58f1-bb80-d2c871785c37",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MScizorEX.Name",
    display_name="M Scizor-EX",
    searchable_by=["M Scizor-EX", "MEGA", "EX", "MScizorEX"],
    subtypes=["MEGA", "EX"],
    collector_number=120,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorEX.Name",
    family_id=212,
    abilities=[
        Attack(
            title="Iron Crusher",
            game_text="You may discard a Special Energy attached to your opponent's Active Pok\u00e9mon or a Stadium card in play.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)