from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import venture_bomb

card = ItemCardDef(
    guid="fda50f24-bb24-5446-95a7-f8f29acd2ea4",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VentureBomb.Name",
    display_name="Venture Bomb",
    searchable_by=["Venture Bomb", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=93,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=venture_bomb,
)
