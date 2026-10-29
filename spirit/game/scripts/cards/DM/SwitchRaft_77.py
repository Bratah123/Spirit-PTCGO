from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import switch_raft, switch_raft_condition

card = ItemCardDef(
    guid="2ed35178-8ed0-5430-a25a-0248454daed4",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwitchRaft.Name",
    display_name="Switch Raft",
    searchable_by=["Switch Raft", "Item"],
    subtypes=["Item"],
    collector_number=77,
    set_code="DM",
    rarity=Rarities.RareSecret,
    effect=switch_raft,
    condition=switch_raft_condition,
)
