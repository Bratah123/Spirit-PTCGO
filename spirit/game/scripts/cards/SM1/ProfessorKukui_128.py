from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier
from spirit.game.card_effects.trainers import deck_nonempty


async def _professor_kukui(ctx):
    """Draw 2 cards. This turn, your Pokemon's attacks do 20 more damage to the
    opponent's Active Pokemon (before Weakness and Resistance)."""
    await ctx.draw_cards(2)
    ctx.add_turn_damage_modifier(TurnDamageModifier(20, ctx.player_id))


card = SupporterCardDef(
    guid="1a6ed5b9-7cf5-5a75-a2dd-8cce5b230615",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorKukui.Name",
    display_name="Professor Kukui",
    searchable_by=["Professor Kukui", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=_professor_kukui
)
