from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.trainers import opponent_has_bench

card = ItemCardDef(
    guid="0ed8bc93-c59a-5542-93ce-a4649d7ccc9f",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Repel.Name",
    display_name="Repel",
    searchable_by=["Repel", "Item"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=opponent_switches,
    condition=opponent_has_bench
)
