from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import poke_nav
from spirit.game.card_effects.trainers import deck_nonempty


card = ItemCardDef(
    guid="25f127f0-8444-546a-b345-6f585716f5f8",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=poke_nav,
)
