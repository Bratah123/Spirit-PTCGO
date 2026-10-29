from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import fiery_flint, fiery_flint_condition

card = ItemCardDef(
    guid="a3ce3b39-962a-56d9-84b7-72d1dcfdea2a",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name",
    display_name="Fiery Flint",
    searchable_by=["Fiery Flint", "Item"],
    subtypes=["Item"],
    collector_number=76,
    set_code="DM",
    rarity=Rarities.RareSecret,
    effect=fiery_flint,
    condition=fiery_flint_condition,
)
