from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType
from spirit.game.session.effects import is_special_energy


def _sidney_predicate(card):
    trainer_type = card.get_attribute(AttrID.TRAINER_TYPE)
    return trainer_type in (TrainerType.POKEMON_TOOL.value, TrainerType.STADIUM.value) \
        or is_special_energy(card)


async def sidney(ctx):
    """Opponent reveals their hand; discard up to 2 Tool/Special Energy/Stadium cards from it."""
    hand = ctx.hand(ctx.opponent_id)
    matches = [c for c in hand if _sidney_predicate(c)]
    picks = await ctx.choose_cards(
        matches, 2, minimum=0,
        prompt="Choose up to 2 cards to discard from your opponent's hand.",
        display_cards=hand,
    )
    await ctx.discard_cards(picks)


card = SupporterCardDef(
    guid="03af20bf-db82-5124-8acb-4a23f6c6a7c5",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sidney.Name",
    display_name="Sidney",
    searchable_by=["Sidney", "Supporter"],
    subtypes=["Supporter"],
    collector_number=241,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=sidney
)
