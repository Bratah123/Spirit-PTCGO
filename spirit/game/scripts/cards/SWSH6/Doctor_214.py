from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.pokemon import is_pokemon_vmax


async def doctor(ctx):
    """Draw 2 cards. If your opponent's Active Pokemon is a Pokemon VMAX, draw 2 more cards."""
    await ctx.draw_cards(2)
    active = ctx.opponent_active()
    if active is not None and is_pokemon_vmax(active.archetype_id):
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="ac7deda3-133e-513e-8529-a4d3d394b9c5",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Doctor.Name",
    display_name="Doctor",
    searchable_by=["Doctor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    effect=doctor,
)
