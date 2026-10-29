from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import switch_raft, switch_raft_condition

card = ItemCardDef(
    guid="09cc0b2d-be04-5aa3-804c-e300eb45ab0c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwitchRaft.Name",
    display_name="Switch Raft",
    searchable_by=["Switch Raft", "Item"],
    subtypes=["Item"],
    collector_number=62,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=switch_raft,
    condition=switch_raft_condition,
)
