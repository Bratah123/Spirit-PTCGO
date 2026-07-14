from spirit.game.card_effects.support_common import requires_discard
from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.session.effects import is_pokemon_card
from spirit.game.attributes import Rarities


async def familiar_bell(ctx):
    """Search your deck for a Pokemon with the same name as a Pokemon in your
    discard pile, reveal it, and put it into your hand. Then, shuffle."""
    discard_names = {
        def_for(c.archetype_id).display_name
        for c in ctx.discard_pile()
        if is_pokemon_card(c) and def_for(c.archetype_id) is not None
    }
    discard_names.discard(None)
    if not discard_names:
        return

    def matches(card):
        if not is_pokemon_card(card):
            return False
        definition = def_for(card.archetype_id)
        return definition is not None and definition.display_name in discard_names

    picks = await ctx.search_deck(
        matches, count=1, minimum=0,
        prompt="Choose a Pokémon with the same name as one in your discard pile.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="70864958-656e-5a6e-91c3-25614cc5bf30",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FamiliarBell.Name",
    display_name="Familiar Bell",
    searchable_by=["Familiar Bell", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    condition=requires_discard(is_pokemon_card),
    effect=familiar_bell,
)
