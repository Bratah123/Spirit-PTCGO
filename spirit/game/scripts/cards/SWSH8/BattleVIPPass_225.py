from spirit.game.card_effects.trainers import battle_vip_pass, battle_vip_pass_playable
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="232d41a8-5a91-5bbd-af9b-310fd169c801",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleVIPPass.Name",
    display_name="Battle VIP Pass",
    searchable_by=["Battle VIP Pass", "Item"],
    subtypes=["Item"],
    collector_number=225,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=battle_vip_pass,
    condition=battle_vip_pass_playable
)
