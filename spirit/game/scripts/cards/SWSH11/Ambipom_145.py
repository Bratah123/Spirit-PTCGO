from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand


async def all_you_can_grab(ctx):
    """Flip until tails; search that many cards into hand, then shuffle."""
    heads = await ctx.flip_until_tails("All-You-Can-Grab")
    if heads > 0:
        picks = await ctx.search_deck(
            count=heads, minimum=0,
            prompt=f"Choose up to {heads} cards to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def knock_off(ctx):
    """50 damage, then discard a random card from the opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="12794499-aaf7-5ab6-9b04-0c01e7ade512",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1", "Ambipom"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Attack(
            title="All-You-Can-Grab",
            game_text="Flip a coin until you get tails. Search your deck for a number of cards up to the number of heads and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=all_you_can_grab,
        ),
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=knock_off,
        ),
    ],
)