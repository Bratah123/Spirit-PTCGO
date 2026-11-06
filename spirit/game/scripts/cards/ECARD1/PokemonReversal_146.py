from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_bench, play_targets


async def pokemon_reversal(ctx):
    """Choose 1 opponent Bench; flip heads → switch with Defending."""
    # play_targets already selected the bench Pokemon into ctx.targets
    targets = list(getattr(ctx, "targets", None) or [])
    if not targets:
        bench = ctx.opponent_bench()
        if not bench:
            return
        chosen = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon")
        if chosen is None:
            return
        targets = [chosen]
    results = await ctx.flip_coins(1, "Pokémon Reversal")
    if not results or not results[0]:
        return
    await ctx.switch_active(ctx.opponent_id, targets[0])


card = ItemCardDef(
    guid="f97bcd3a-7386-5f0e-a5c4-3cb20f8c858c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pokémon Reversal"],
    subtypes=[],
    collector_number=146,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=pokemon_reversal,
    play_targets=play_targets(opponent=True, bench_only=True),
    play_target_prompt="Choose 1 of your opponent's Benched Pokémon",
    condition=opponent_has_bench,
)
