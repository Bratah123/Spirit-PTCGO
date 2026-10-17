"""STUB: effect not implemented — do not guess mechanics.
Evosoda (XY1 #116): trainer effect stubbed.

Card text:
  - Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward. You can't use this card during your first turn or on a Pokémon that was put into play this turn.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="180b57c2-e73c-5589-86fb-7242717055e6",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evosoda.Name",
    display_name="Evosoda",
    searchable_by=["Evosoda", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
