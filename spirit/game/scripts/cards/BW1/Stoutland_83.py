from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def odor_sleuth(ctx):
    """Flip 3 coins. For each heads, put a card from discard into hand."""
    results = await ctx.flip_coins(3, "Odor Sleuth")
    heads = sum(1 for r in results if r)
    if heads <= 0:
        return
    discard = list(ctx.discard_pile())
    if not discard:
        return
    count = min(heads, len(discard))
    picks = await ctx.choose_cards(
        discard, count, minimum=count,
        prompt=f"Choose {count} card(s) from your discard pile",
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="ccf58a40-604c-54c8-97ce-cd1b1e678faf",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=83,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Attack(
            title="Odor Sleuth",
            game_text="Flip 3 coins. For each heads, put a card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=odor_sleuth,
        ),
        Attack(
            title="Giga Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            locks_next_turn=True,
        ),
    ],
)
