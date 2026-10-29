from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    poke_nav,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="04c8d539-e29e-5004-9b73-2a8b785cbc48",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=poke_nav,
    condition=deck_nonempty,
)
