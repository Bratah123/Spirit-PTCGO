"""STUB: effect not implemented — do not guess mechanics.
M Charizard-EX (XY12 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="182cf86a-28d6-5896-b0dc-356917360f9a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MCharizardEX.Name",
    display_name="M Charizard-EX",
    searchable_by=["M Charizard-EX", "MEGA", "EX", "MCharizardEX"],
    subtypes=["MEGA", "EX"],
    collector_number=13,
    set_code="XY12",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Crimson Dive",
            game_text="This Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 3},
            damage=300,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)