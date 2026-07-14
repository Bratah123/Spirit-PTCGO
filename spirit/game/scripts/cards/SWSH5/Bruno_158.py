from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def bruno(ctx):
    """Shuffle hand into deck; draw 4, or 7 if a Pokémon of yours was Knocked Out during the opponent's last turn."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    count = 7 if ctx.kos_suffered_last_turn() else 4
    await ctx.draw_cards(count)


card = SupporterCardDef(
    guid="64ffaa7b-3b51-5255-9d54-fca0f339e064",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bruno.Name",
    display_name="Bruno",
    searchable_by=["Bruno", "Supporter", "Single Strike"],
    subtypes=["Supporter", "Single Strike"],
    collector_number=158,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    effect=bruno,
)
