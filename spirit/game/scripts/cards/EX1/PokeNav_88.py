from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import poke_nav
from spirit.game.card_effects.trainers import deck_nonempty


card = ItemCardDef(
    guid="1aea3327-5b65-5f73-a3ca-bd2822bd2c45",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=poke_nav,
)
