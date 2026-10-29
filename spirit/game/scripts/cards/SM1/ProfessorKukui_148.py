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
    guid="30a2b596-dc83-5a33-b1cf-40ba5f7d9405",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorKukui.Name",
    display_name="Professor Kukui",
    searchable_by=["Professor Kukui", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    effect=_professor_kukui
)
