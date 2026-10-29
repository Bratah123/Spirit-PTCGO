from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    poke_nav,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="457c7e1e-431b-5ea9-a9a2-aafba43a9d11",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    effect=poke_nav,
    condition=deck_nonempty,
)
