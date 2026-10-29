from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import fiery_flint, fiery_flint_condition

card = ItemCardDef(
    guid="ac6e3f7b-147d-5e49-93da-042959e0f6e6",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name",
    display_name="Fiery Flint",
    searchable_by=["Fiery Flint", "Item"],
    subtypes=["Item"],
    collector_number=60,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=fiery_flint,
    condition=fiery_flint_condition,
)
