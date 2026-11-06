from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.trainers import deck_nonempty


def _name(card):
    return getattr(def_for(card.archetype_id), "display_name", None)


async def repeat_ball(ctx):
    """Search your deck for a Pokemon with the same name as 1 of your Pokemon
    in play, reveal it, and put it into your hand. Shuffle."""
    names = {_name(p) for p in ctx.my_pokemon_in_play()}
    picks = await ctx.search_deck(lambda c: is_pokemon_card(c) and _name(c) in names,
                                  count=1, minimum=0, prompt="Choose a Pokémon")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="599e6d4f-7a60-578c-a17d-20f2d1c1eef0",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RepeatBall.Name",
    display_name="Repeat Ball",
    searchable_by=["Repeat Ball", "Item"],
    subtypes=["Item"],
    collector_number=136,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=repeat_ball,
    condition=deck_nonempty
)
