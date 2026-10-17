"""STUB: effect not implemented — do not guess mechanics.
M Gardevoir-EX (XY11 #112): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="187d88d4-f2bf-5f58-8dec-1765979e0418",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGardevoirEX.Name",
    display_name="M Gardevoir-EX",
    searchable_by=["M Gardevoir-EX", "MEGA", "EX", "MGardevoirEX"],
    subtypes=["MEGA", "EX"],
    collector_number=112,
    set_code="XY11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FAIRY, PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    family_id=282,
    abilities=[
        Attack(
            title="Despair Ray",
            game_text="Discard as many of your Benched Pok\u00e9mon as you like. This attack does 10 more damage for each Benched Pok\u00e9mon you discarded in this way.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)