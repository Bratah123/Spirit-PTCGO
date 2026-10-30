from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import battle_frontier_passive

card = StadiumCardDef(
    guid="863670df-0f40-501c-b9ec-f262b7db8a19",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleFrontier.Name",
    display_name="Battle Frontier",
    searchable_by=["Battle Frontier", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    passive=battle_frontier_passive(),
)
