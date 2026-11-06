from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _evil_orders(ctx):
    """Search your deck for up to (number of your Benched Pokemon) cards; shuffle."""
    n = len(ctx.my_bench())
    if n > 0:
        picks = await ctx.search_deck(None, count=n, minimum=0,
                                      prompt=f"Choose up to {n} card(s) to put into your hand.")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ac2f4563-74c7-5d3d-b95f-1c0af2c80587",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaticate.Name",
    display_name="Alolan Raticate",
    searchable_by=["Alolan Raticate", "Stage 1", "AlolanRaticate"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Evil Orders",
            game_text="Search your deck for a number of cards up to the number of your Benched Pok\u00e9mon and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_evil_orders,
        ),
        Attack(
            title="Endeavor",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=30),
        ),
    ],
)