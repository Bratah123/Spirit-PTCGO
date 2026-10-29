from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import fiery_flint, fiery_flint_condition

card = ItemCardDef(
    guid="11a64d81-279d-50cb-b505-2c853702f65c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name",
    display_name="Fiery Flint",
    searchable_by=["Fiery Flint", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=fiery_flint,
    condition=fiery_flint_condition,
)
