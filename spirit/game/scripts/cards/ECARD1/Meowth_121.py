from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _pay_day(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Pay Day")
    if results and results[0]:
        await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="3ed4b12c-35c3-56df-9f50-93fb193969c7",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Pay Day",
            game_text="Flip a coin. If heads, draw a card.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=_pay_day,
        ),
    ],
)
