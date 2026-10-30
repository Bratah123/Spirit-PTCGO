from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import pow_hand_extension

card = ItemCardDef(
    guid="7e5e9565-b7a2-5ea7-9eab-5f90610f75d8",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowHandExtension.Name",
    display_name="Pow! Hand Extension",
    searchable_by=["Pow! Hand Extension", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=85,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=pow_hand_extension,
)
