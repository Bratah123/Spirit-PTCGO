from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import battle_frontier_passive

card = StadiumCardDef(
    guid="4e1b06fc-c7c4-5dc7-8ae5-06313ea4bbdd",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleFrontier.Name",
    display_name="Battle Frontier",
    searchable_by=["Battle Frontier", "Stadium"],
    subtypes=["Stadium"],
    collector_number=71,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=battle_frontier_passive(),
)
