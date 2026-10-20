from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench, play_targets


async def scramble_switch(ctx):
    """ACE SPEC: switch your Active Pokemon with 1 of your Benched Pokemon,
    then move as many Energy from the old Active to the new one as you like."""
    old = ctx.my_active()
    target = await ctx.choose_play_target(ctx.my_bench(), "Choose your new Active Pokémon")
    if target is None or old is None:
        return
    if not await ctx.switch_active(ctx.player_id, target):
        return
    energies = ctx.attached_energies(old)
    if not energies:
        return
    picks = await ctx.choose_cards(energies, len(energies), minimum=0,
                                   prompt="Choose Energy to move to your new Active Pokémon")
    for energy in picks or []:
        await ctx.move_energy(energy, target)


card = ItemCardDef(
    guid="1c6fa5b8-b93f-5a1a-86fe-f78e09f1b00f",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScrambleSwitch.Name",
    display_name="Scramble Switch",
    searchable_by=["Scramble Switch", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=129,
    set_code="BW8",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=scramble_switch,
    play_targets=play_targets(opponent=False, bench_only=True),
    play_target_prompt="",
    condition=player_has_bench
)
