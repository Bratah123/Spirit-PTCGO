from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _electric_mischief(ctx):
    """Flip 3 coins; for each heads, a random card from your opponent's hand
    is revealed and shuffled into their deck."""
    import random
    results = await ctx.flip_coins(3, ctx.ability.title)
    picks = []
    for r in results or []:
        hand = [c for c in ctx.hand(ctx.opponent_id) if c not in picks]
        if r and hand:
            picks.append(random.choice(hand))
    if picks:
        await ctx.reveal_cards(picks)
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = PokemonCardDef(
    guid="ec32a305-da81-5962-9ccf-88cee9a4be19",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=479,
    abilities=[
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Electric Mischief",
            game_text="Flip 3 coins. For each heads, choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_electric_mischief,
        ),
    ],
)