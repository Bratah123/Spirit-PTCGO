from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per, count_energy


async def gritty_comeback(ctx):
    """Switch all damage counters on this Pokemon with those on the opponent's Active."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    self_counters = damage_counters_on("self")(ctx)
    opp_counters = damage_counters_on("defender")(ctx)
    await ctx.set_damage_counters(ctx.source, opp_counters)
    await ctx.set_damage_counters(defender, self_counters)


card = PokemonCardDef(
    guid="4ef34723-3ff6-599f-8864-a9998d6226ea",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    display_name="Mewtwo-EX",
    searchable_by=["Mewtwo-EX", "Basic", "EX", "MewtwoEX"],
    subtypes=["Basic", "EX"],
    collector_number=164,
    set_code="XY8",
    rarity=Rarities.RareSecret,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Shatter Shot",
            game_text="This attack does 30 damage times the amount of Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.PSYCHIC), 30),
        ),
        Attack(
            title="Damage Change",
            game_text="Switch all damage counters on this Pok\u00e9mon with those on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=gritty_comeback,
        ),
    ],
)