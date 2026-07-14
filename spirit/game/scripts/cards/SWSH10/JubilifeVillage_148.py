from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities


async def jubilife_village(ctx):
    """Shuffle your hand into your deck and draw 5 cards. Your turn ends."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(5)
    ctx.ends_turn = True


JUBILIFE_VILLAGE_ABILITY = Ability(
    title="Jubilife Village",
    game_text="Once during each player's turn, that player may shuffle their hand into their deck and draw 5 cards. If they do, their turn ends.",
    activation=Activations.ONCE_PER_TURN,
    effect=jubilife_village,
)

card = StadiumCardDef(
    guid="c8a8c5b4-17b9-5a9d-b3a9-75510d15411f",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JubilifeVillage.Name",
    display_name="Jubilife Village",
    searchable_by=["Jubilife Village", "Stadium"],
    subtypes=["Stadium"],
    collector_number=148,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    ability=JUBILIFE_VILLAGE_ABILITY,
)
