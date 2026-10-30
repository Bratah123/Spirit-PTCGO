from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import lysandre_labs_passive

card = StadiumCardDef(
    guid="f885b1a4-7263-52f1-99a1-7d0e9e26edb8",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandreLabs.Name",
    display_name="Lysandre Labs",
    searchable_by=["Lysandre Labs", "Stadium"],
    subtypes=["Stadium"],
    collector_number=111,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    passive=lysandre_labs_passive,
)
