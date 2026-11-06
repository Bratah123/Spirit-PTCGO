from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import flip_draw, has_cards_in_deck


card = ItemCardDef(
    guid="47e96095-de5b-5f8d-8798-45ccfed56b02",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsTeleporter.Name",
    display_name="Bill's Teleporter",
    searchable_by=["Bill's Teleporter"],
    subtypes=[],
    collector_number=91,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=flip_draw(4),
)
