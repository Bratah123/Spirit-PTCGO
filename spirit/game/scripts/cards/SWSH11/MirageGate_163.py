from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import mirage_gate, mirage_gate_condition

card = ItemCardDef(
    guid="4f434571-544d-504f-9d72-861beabdb614",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MirageGate.Name",
    display_name="Mirage Gate",
    searchable_by=["Mirage Gate", "Item"],
    subtypes=["Item"],
    collector_number=163,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    condition=mirage_gate_condition,
    effect=mirage_gate,
)
