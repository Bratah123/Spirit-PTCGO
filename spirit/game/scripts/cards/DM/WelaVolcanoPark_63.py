from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import wela_volcano_park_passive

card = StadiumCardDef(
    guid="dd8595de-b606-5d37-94d8-ce36fbed6758",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WelaVolcanoPark.Name",
    display_name="Wela Volcano Park",
    searchable_by=["Wela Volcano Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=63,
    set_code="DM",
    rarity=Rarities.Uncommon,
    passive=wela_volcano_park_passive,
)
