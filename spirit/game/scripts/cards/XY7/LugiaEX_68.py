from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy


_mine = count_energy('self')
_theirs = count_energy('defender')


async def _aero_ball(ctx):
    """20x the amount of Energy attached to both Active Pokemon."""
    await ctx.deal_damage(20 * (_mine(ctx) + _theirs(ctx)))


async def _deep_hurricane(ctx):
    """80+; +70 if any Stadium is in play, then discard it."""
    if ctx.stadium_in_play() is None:
        await ctx.deal_damage()
        return
    await ctx.deal_damage(ctx.ability.damage + 70)
    await ctx.discard_stadium()


card = PokemonCardDef(
    guid="396fed67-66bf-5c52-b0ef-074ad11fe90a",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaEX.Name",
    display_name="Lugia-EX",
    searchable_by=["Lugia-EX", "Basic", "EX", "LugiaEX"],
    subtypes=["Basic", "EX"],
    collector_number=68,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=249,
    abilities=[
        Attack(
            title="Aero Ball",
            game_text="This attack does 20 damage times the amount of Energy attached to both Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=_aero_ball,
        ),
        Attack(
            title="Deep Hurricane",
            game_text="If there is any Stadium card in play, this attack does 70 more damage. Then, discard that Stadium card.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator="+",
            effect=_deep_hurricane,
        ),
    ],
)