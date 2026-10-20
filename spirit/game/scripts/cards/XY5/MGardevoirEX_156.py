"""STUB: effect not implemented — do not guess mechanics.
M Gardevoir-EX (XY5 #156): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd551de2-662e-5fc8-a552-89b467d3dac9",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGardevoirEX.Name",
    display_name="M Gardevoir-EX",
    searchable_by=["M Gardevoir-EX", "MEGA", "EX", "MGardevoirEX"],
    subtypes=["MEGA", "EX"],
    collector_number=156,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    family_id=282,
    abilities=[
        Attack(
            title="Brilliant Arrow",
            game_text="This attack does 30 damage times the amount of Fairy Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)