from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def ransack(ctx):
    """Flip 2. If any heads, opponent reveals hand; for each heads, choose a
    card there and put it on the bottom of their deck, in any order."""
    coins = await ctx.flip_coins(2, "Ransack")
    heads = coins.count(True)
    if heads == 0:
        return
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, heads, ordered=True,
        prompt="Choose cards from your opponent's hand to put on the bottom of their deck, in any order.",
    )
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)


card = PokemonCardDef(
    guid="9d55755b-a5ee-5e26-b743-07730c67d4cb",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Ransack",
            game_text="Flip 2 coins. If either of them is heads, your opponent reveals their hand. For each heads, choose a card you find there and put it on the bottom of your opponent's deck in any order.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ransack,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)