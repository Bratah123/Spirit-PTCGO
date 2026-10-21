from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_trainer_card
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.trainers import deck_nonempty


def _mailable(card):
    return is_trainer_card(card) and getattr(def_for(card.archetype_id), "display_name", None) != "Trainers' Mail"


async def trainers_mail(ctx):
    """Look at the top 4 cards of your deck; you may reveal a Trainer card
    (except Trainers' Mail) and put it into your hand. Shuffle the rest back."""
    top = ctx.deck_top(4)
    pool = [c for c in top if _mailable(c)]
    picks = await ctx.choose_cards(pool, 1, minimum=0, display_cards=top,
                                   prompt="Choose a Trainer card") if pool else []
    if not pool and top:
        await ctx.choose_cards(top, 1, minimum=0, display_cards=top, prompt="No Trainer cards")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="9b0e3c49-0f2a-546b-bbcb-2811bc706407",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainersMail.Name",
    display_name="Trainers' Mail",
    searchable_by=["Trainers' Mail", "Item"],
    subtypes=["Item"],
    collector_number=112,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=trainers_mail,
    condition=deck_nonempty
)
