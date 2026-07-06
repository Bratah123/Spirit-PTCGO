from spirit.game.card_effects.trainers import deck_nonempty, rotom_phone
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="665d809c-cfea-5e4f-bddf-b5131c05d4a7",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RotomPhone.Name",
    display_name="Rotom Phone",
    searchable_by=["Rotom Phone", "Item"],
    subtypes=["Item"],
    collector_number=64,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=rotom_phone,
    condition=deck_nonempty
)
