from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


_own_counters = damage_counters_on('self')


async def _crimson_edge(ctx):
    """180; this Pokemon does 10 damage to itself for each damage counter on it."""
    await ctx.deal_damage()
    n = _own_counters(ctx)
    if n:
        await ctx.deal_damage(10 * n, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="280886af-32ed-5595-9cb8-54ebe102ad14",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGarchompEX.Name",
    display_name="M Garchomp-EX",
    searchable_by=["M Garchomp-EX", "MEGA", "EX", "MGarchompEX"],
    subtypes=["MEGA", "EX"],
    collector_number=168,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompEX.Name",
    family_id=445,
    abilities=[
        Attack(
            title="Crimson Edge",
            game_text="This Pok\u00e9mon does 10 damage to itself for each damage counter on it.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=_crimson_edge,
        ),
    ],
)