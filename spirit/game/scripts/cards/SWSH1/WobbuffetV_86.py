from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


async def gritty_comeback(ctx):
    """Switch all damage counters on this Pokemon with those on the opponent's Active."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    self_counters = damage_counters_on("self")(ctx)
    opp_counters = damage_counters_on("defender")(ctx)
    await ctx.set_damage_counters(ctx.source, opp_counters)
    await ctx.set_damage_counters(defender, self_counters)


async def shadow_bind(ctx):
    """70 damage. During your opponent's next turn, the Defending Pokemon can't retreat."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="23132b90-ec25-5146-9f8c-785d228719cb",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WobbuffetV.Name",
    display_name="Wobbuffet V",
    searchable_by=["Wobbuffet V", "Basic", "V", "WobbuffetV"],
    subtypes=["Basic", "V"],
    collector_number=86,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=202,
    abilities=[
        Attack(
            title="Gritty Comeback",
            game_text="Switch all damage counters on this Pok\u00e9mon with those on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=gritty_comeback,
        ),
        Attack(
            title="Shadow Bind",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=70,
            effect=shadow_bind,
        ),
    ],
)