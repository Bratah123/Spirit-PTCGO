from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


async def _big_bang_horn(ctx):
    """180 minus 10 for each damage counter on this Pokemon."""
    await ctx.deal_damage(max(0, 180 - 10 * damage_counters_on('self')(ctx)))


card = PokemonCardDef(
    guid="f4de6e3b-bdcc-52ff-b176-1a8b8dceacc7",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MHeracrossEX.Name",
    display_name="M Heracross-EX",
    searchable_by=["M Heracross-EX", "MEGA", "EX", "MHeracrossEX"],
    subtypes=["MEGA", "EX"],
    collector_number=5,
    set_code="XY3",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HeracrossEX.Name",
    family_id=214,
    abilities=[
        Attack(
            title="Big Bang Horn",
            game_text="This attack does 180 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            damage_operator="-",
            effect=_big_bang_horn,
        ),
    ],
)