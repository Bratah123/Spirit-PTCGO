from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1c6fa5b8-b93f-5a1a-86fe-f78e09f1b00f",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScrambleSwitch.Name",
    display_name="Scramble Switch",
    searchable_by=["Scramble Switch", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=129,
    set_code="BW8",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
