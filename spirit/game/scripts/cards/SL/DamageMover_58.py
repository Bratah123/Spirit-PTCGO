from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sl import damage_mover, damage_mover_condition

card = ItemCardDef(
    guid="dc28221b-6481-5d1c-b2a9-209682844fad",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DamageMover.Name",
    display_name="Damage Mover",
    searchable_by=["Damage Mover", "Item"],
    subtypes=["Item"],
    collector_number=58,
    set_code="SL",
    rarity=Rarities.Uncommon,
    condition=damage_mover_condition,
    effect=damage_mover,
)
