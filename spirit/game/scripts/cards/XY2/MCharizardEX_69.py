"""STUB: effect not implemented — do not guess mechanics.
M Charizard-EX (XY2 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3f0dea4-804c-5484-88ed-3d1821821e54",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MCharizardEX.Name",
    display_name="M Charizard-EX",
    searchable_by=["M Charizard-EX", "MEGA", "EX", "MCharizardEX"],
    subtypes=["MEGA", "EX"],
    collector_number=69,
    set_code="XY2",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Wild Blaze",
            game_text="Discard the top 5 cards of your deck.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=300,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)