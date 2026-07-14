from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_item_card


def _is_ball_item(card):
    if not is_item_card(card):
        return False
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return bool(definition and "ball" in (definition.display_name or "").lower())


async def ball_guy(ctx):
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    seen_names = set()
    for card_entity in deck_cards:
        if not _is_ball_item(card_entity):
            continue
        definition = def_for(card_entity.archetype_id)
        name = definition.display_name if definition else None
        if not name or name in seen_names:
            continue
        seen_names.add(name)
        reps.append(card_entity)
    picks = await ctx.choose_cards(
        reps, 3, minimum=0,
        prompt="Choose up to 3 different Item cards with \"Ball\" in their name.",
        display_cards=deck_cards,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="781b22f5-be57-549e-a72e-3380392bf826",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BallGuy.Name",
    display_name="Ball Guy",
    searchable_by=["Ball Guy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=65,
    set_code="SWSH45",
    rarity=Rarities.RareUltra,
    effect=ball_guy,
)
