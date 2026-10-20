from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import guts_survive_passive


async def _bide(ctx):
    """Flip; heads: if this Pokemon would be KO'd by attack damage during the
    opponent's next turn, it isn't and its remaining HP becomes 10."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, guts_survive_passive(hp_floor=10, title="Bide", flip=False))


card = PokemonCardDef(
    guid="2c68a175-d1c7-5ef8-84fe-1fcf1619f744",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    display_name="Seedot",
    searchable_by=["Seedot", "Basic", "Seedot"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=273,
    abilities=[
        Attack(
            title="Bide",
            game_text="Flip a coin. If heads, if this Pok\u00e9mon would be Knocked Out by damage from an attack during your opponent's next turn, it is not Knocked Out and its remaining HP becomes 10 instead.",
            cost={PokemonTypes.GRASS: 1},
            effect=_bide,
        ),
    ],
)