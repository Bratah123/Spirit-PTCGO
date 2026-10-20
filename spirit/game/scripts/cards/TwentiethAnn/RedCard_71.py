"""STUB: effect not implemented — do not guess mechanics.
Red Card (TwentiethAnn #71): trainer effect stubbed.

Card text:
  - Your opponent shuffles his or her hand into his or her deck and draws 4 cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e5e855ca-2af9-536e-a349-7dcf5d43bfc1",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RedCard.Name",
    display_name="Red Card",
    searchable_by=["Red Card", "Item"],
    subtypes=["Item"],
    collector_number=71,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
