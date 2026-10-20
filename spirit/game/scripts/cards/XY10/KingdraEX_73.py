"""STUB: effect not implemented — do not guess mechanics.
Kingdra-EX (XY10 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _gaia_crush(ctx):
    """Printed damage; discard any Stadium card in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="82fcf1da-1c63-56dc-8673-6b4d6e0a25ce",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KingdraEX.Name",
    display_name="Kingdra-EX",
    searchable_by=["Kingdra-EX", "Basic", "EX", "KingdraEX"],
    subtypes=["Basic", "EX"],
    collector_number=73,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=230,
    abilities=[
        Attack(
            title="Big Storm",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=_gaia_crush,
        ),
        Attack(
            title="Dragon Trail",
            game_text="This attack does 30 more damage for each basic Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)